# 事件契约 v4（Event Contract v4）

- 状态：定稿待实施（实施时转 JSON Schema：`schema/event-contract-v4.schema.json`）
- 依据：multi-axis-verdict spec §5 + autoplan 终门 D1（事件流替代轴固化）
- 核心原则：**事件是不可变事实，判定是派生视图**。schema 只约束事实结构，不固化判定结构——
  下次生态争议改的是视图层，不再升契约。

## 1. 三类事件

所有事件共享信封（envelope）+ 各自 payload：

```jsonc
{
  "event": "install_attempt",            // install_attempt | boot_attempt | function_probe
  "event_id": "uuid4",
  "observed_at": "ISO8601",
  "supersedes": "event_id | null",       // 修正=新事件指旧事件；原事件永不改写
  "candidate": {                          // —— 信封：主体标识 ——
    "local_key": "...", "canonical_id": "...",
    "repo_commit": "...", "package_integrity": "sha256:..."
  },
  "environment": {                        // —— 信封：环境指纹（还 README:259 历史债）——
    "dsh_version": "...", "node_version": "...", "pnpm_version": "...",
    "runner_image_digest": "...", "profile": "...",
    "network_policy_revision": "...",     // 双沙箱策略版本（④）
    "contract_revision": 4
  },
  "payload": { /* 见下 */ }
}
```

### 1.1 install_attempt

```jsonc
{
  "resolver": "published | independent",        // 双轨（①）：站点发布命令 vs 我方独立解析
  "resolver_snapshot_sha": "...",               // published 轨锚站点快照（stale 可追溯）
  "install_spec": "npm:pkg@ver | github:o/r | tarball:url",
  "source_kind": "npm | github | tarball",
  "attempt": {
    "first":  { "verdict": "pass|fail|blocked|timeout",
                "error_code": "ERR_PNPM_* | ...", "error_tail": "≤4000B",
                "duration_s": 0, "allow_builds_required": false,
                "blocked_packages": ["node-pty@1.1.0"] },   // ② 三态的机器事实
    "approved": null                              // 授权复测（仅在④沙箱就绪后产生）
                // { "verdict": "...", "sandbox_class": "install", ... }
  }
}
```

### 1.2 boot_attempt

```jsonc
{
  "profile": "headless | web | pty",             // ③ 分型
  "escalated_from": "profile | null",            // 首形态失败升级路径（web←headless）
  "verdict": "booted | crashed | env-unsupported",
  "readiness_probe": "url_line | boot_manifest | ...",
  "error_tail": "≤4000B", "duration_s": 0
}
```

### 1.3 function_probe

```jsonc
{
  "probe_class": "deterministic | model",        // L3a | L3b（③去模型化的分界）
  "deterministic": { "checks": [...], "verdict": "..." },   // L3a：脚本可验
  "model": {                                     // L3b：独立标注，不入确定性结论
    "verdict": "...", "model_id": "...", "prompt_revision": "...",
    "raw_output_ref": "..."                      // agent 原始输出落盘引用（可审计）
  }
}
```

## 2. 派生视图（渲染层，不在本契约内）

- 用户视图（D2 主受众）：`published 轨 first.verdict + approved?.verdict` →
  ✅ 开箱即用 / ⚠️ 需构建授权 / ❌ 硬失败
- 审计视图（作者）：两轨 install_attempt 对照 + boot/function 事件明细
- 治理视图：needs-review 队列（⑤状态机）
- divergence 信号：published vs independent 的 install verdict 不一致 →
  `divergence_kind: npm_tarball_contains_build_artifacts | resolver_stale | ...`

## 3. 演算验证（#2582 反例）

`dsh-context`（npm 制品好 / git 源缺构建产物）在新契约下：

```
install_attempt #1: resolver=published, spec=npm:dsh-context@x.y → first.verdict=pass
install_attempt #2: resolver=independent, spec=github:bowenliang123/dsh-context
                   → first.verdict=fail, error_code=ERR_MODULE_NOT_FOUND(dist/)
boot_attempt     : profile=web → booted
```

两个 install 事实并存不覆盖；用户视图取 published 轨（✅）；审计视图呈现 divergence 信号。
旧契约的「FAIL」与站点的「PASS」之争在新模型下是两条互不冲突的记录。

## 4. 迁移锚

- `RESULT_CONTRACT_REVISION=4` 进 input_hash（现有机制）→ 部署即全量重测，旧判定标 `legacy`
- 事件存储：每候选一个 append-only JSONL（`.rt-agent-v2/events/<local_key>.jsonl`），
  与现有 results/*.json 并存过渡一个契约周期
- 哨兵（B3）校验事件流的 expected 事件序列，而非单一 verdict
