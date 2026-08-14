# Agent 运行级插件测试（k8s + dsh + Qwen）

把"插件能不能在真实 dsh 里加载"这件事，从**手写 symlink+patch 的脚本**（过去 100% 误报"加载失败、分不清真假"）升级为：**容器内 dsh 当 agent、用 Qwen 读插件 README、自主按文档导入并验证**，3 次重试全败才判不兼容。

## 架构

```
kind 集群（10.144.144.9，docker 里跑 k8s，免 sudo）
└─ indexed Job（parallelism=completions=5，每 pod 一个分片）
   └─ pod（hostNetwork → 直连 Qwen）
      ├─ dsh（agent 框架，原生支持 OpenAI 兼容的 Qwen；非 root）
      ├─ de-stream 代理（localhost:18093）：dsh stream=True → Qwen stream=False → 重包 SSE
      ├─ /clones（宿主插件 shallow clone，只读）
      ├─ /dsh-home（宿主 ~/.dsh profile，拷成可写私有副本）
      └─ /radar（宿主 repo：写 .rt-agent/<plugin>.json 结果）
```

- `shard-runner.sh`：按 `JOB_COMPLETION_INDEX` 把 `/clones` 取模分片，逐个调 `test-plugin-agent.sh`。
- `test-plugin-agent.sh`：起 de-stream 代理 → `dsh --profile headless "<收敛 prompt>"` → 解析 PASS/FAIL → 3 次重试 → 写 `.rt-agent/<plugin>.json`。
- `aggregate-agent-test.py`（在仓库 `scripts/`）：把 `.rt-agent/*.json` 聚合成 `reports/<日期>/agent-test.md` + `generated/current/agent-results.json`。

## 三层 bug 的定位与修复（最有价值的部分）

初始现象：dsh 的 agent loop 里，Qwen 返回的 tool name **永远为空**（`unknown tool ""`），agent 一步都动不了。直接 curl Qwen 单工具却正常。逐层往下挖：

1. **vLLM 流式 tool_call 的 name 是 null。** 抓 SSE：`stream=True` 时 tool_call chunk 的 `function.name` 为 `null`；同一请求 `stream=False` 时 name 完整。
   → **de-stream 代理**：把 dsh 的流式请求转非流式发给 Qwen，拿到完整 tool_calls 后重包成单个 SSE chunk 回给 dsh。

2. **多轮 400 `Extra data: char 48`。** de-stream 后第一轮能调工具，第二轮起 400。抓 dsh 回传的 assistant 消息：`tool_call.arguments = '{"file_path":"README.md"}{"file_path":"package.json"}'`——Qwen 返回了**并行**两个 read，de-stream 重包丢了 per-call `index`，dsh 把两个参数拼成一个 JSON 字符串。
   → 代理强制 `parallel_tool_calls=false`，每轮只一个工具调用。

3. **不收敛 → EMPTY_RESPONSE。** 修好上面两步后，agent 一轮能跑 60+ 工具调用却不收尾，撑爆上下文返回空。
   → **收紧 prompt**（控制在 ~8 步、完成即出结论，禁止过度调查）。

修完三层，dsh-tool-time 给出**真实可核验**的结论：`FAIL: 缺少 peer 依赖 @deepseek-ai/dsh-tools（内部私有包，npm 不可安装）`——3 次一致。全量 242 插件跑出 **121 ✅可用 / 121 ❌不兼容**（不再是过去 100% 假失败）。

## 怎么跑

```sh
# 1. 建镜像（dsh 预烘，node-pty 需 build-essential）
docker build --network=host -t dsh-test-runner:latest .   # 在本目录

# 2. kind 集群（extraMounts 挂 .clones / repo / .dsh）
kind create cluster --config kind-cfg.yaml   # kind-cfg.yaml 见仓库或自建

# 3. 装镜像 + 起 Job（QWEN_BASE_URL 换成你的 Qwen vLLM 地址）
kind load docker-image dsh-test-runner:latest --name <cluster>
kubectl create ns dsh-test
kubectl apply -f job.yaml

# 4. 跑完聚合
python3 scripts/aggregate-agent-test.py
```

## 前置条件 / 边界

- **Qwen3.6-35B 的 tool-call 必须经 de-stream 代理**（vLLM 流式 bug）；换更强模型可去掉代理。
- profile 来自宿主 `~/.dsh`（含 Qwen model 配置），pod 拷成可写副本避免并发写冲突。
- 浏览器类/重内存插件可能超过 4Gi limit——单独放宽。
- agent 测的是"能否按 README 导入并加载"，不等同于"功能完全正确"；结论是**加载级兼容性**。
