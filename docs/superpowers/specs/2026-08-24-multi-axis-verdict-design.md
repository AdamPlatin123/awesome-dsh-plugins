# 多轴证据系统设计（Multi-Axis Verdict）

- 日期：2026-08-24
- 状态：待用户评审
- 依据：awesome-dsh-plugin/awesome-dsh-plugin#2582 分歧事件 → 外部评审意见（已全文采纳核心修正：④⑤前置、契约先升版、双轨不切权威、多轴替代单判）
- 落点：雷达测试台（现运行于 10.144.144.9，代码副本 /mnt/data/radar/dsh-k8s@192.168.1.152）

## 1. 问题定性

当前雷达把四种本质不同的判定压进一个「可用/不可用」：

```
用户按生态站命令安装是否可用 ≠ GitHub 源码是否可直接安装 ≠ 插件加载是否成功 ≠ 功能是否真的工作
```

#2582 的干净反例：`dsh-context` 等 4 插件 npm 制品可启动、GitHub 源缺构建产物——两种结果同时为真，不应互相覆盖。`allowBuilds` 的 183 例失败语义是「需要用户授权构建」而非「插件坏」。

## 2. 目标 / 非目标

**目标**：雷达从单一兼容性判定器改造为多轴证据系统——每轴独立判定、独立证据、divergence 成为生态质量信号。
**非目标**：与站点测试台互相复制口径。双方共用 user-path contract 后，剩余差异即环境差异，构成 cross-validation；我方独立 resolver 是站点数据的上游异常哨兵。

## 3. 核心数据模型

每个候选插件产出多轴 verdict（不再互相覆盖）：

```
published_path:   PASS | FAIL | ...     # 站点发布命令（npm-map/tarball/github 按站点序）
source_git_path:  PASS | FAIL | ...     # 独立解析（我方 resolver，全部候选）
install_gate:     none | allow_builds   # 首测撞 gate 事实 + 授权后复测结果
boot:             headless/web/pty 分型 # 确定性脚本判
function:
  deterministic_verdict                 # L3a：可脚本验证的尽量脚本
  model_verdict + model_id + prompt_rev # L3b：LLM 体验验证，独立标注
divergence:       published≠source 时记录（如 npm_tarball_contains_build_artifacts）
```

用户侧三档呈现：**✅ 开箱即用 / ⚠️ 需构建授权 / ❌ 硬失败**（授权后仍败或与 gate 无关）。
可发布三个生态指标：开箱安装率 / 构建授权率 / 硬失败率。

## 4. 六项设计

### ① 双轨安装 resolver（不切权威源）
- 站点收录 1837 条：published path（按站点 `data/npm-map.json`+tarball 声明取源，固定 snapshot SHA 锚定）+ independent path 哨兵双跑
- 剩余 ~6000 条：仅 independent path
- **站点 npm-map 不升格真理源**（其映射一经发布即缓存、仅"未发布"态按日重探，有 stale 风险）——我方发现 npm 而站点未映射时：记录 `source_divergence: true`，**不自动修改任何一方**
- 双方 divergence matrix 是 calibration run 的核心产出

### ② allowBuilds 三态
- 机器数据两字段：`first_install {verdict: blocked, reason: allow_builds, packages[]}` + `after_build_approval {verdict}`
- **工程依赖：hardened build sandbox（④）完成前，不开启授权复测轮**——否则只是把 `dangerouslyAllowAllBuilds` 换个名字

### ③ 启动/功能分层去模型化
```
L1 install     纯脚本
L2 load/boot   纯脚本（确定性）
L3a deterministic function probe   能调工具/API 直验的尽量无 LLM
L3b model experience probe         LLM，独立 model-verdict
```
- LLM 彻底退出安装/启动 verdict；「LLM 没选择调用插件」不得解释为功能坏
- **web 按需分型不 blanket**：manifest/capability 判型 → 普通=headless boot；UI/web=web 形态（复现站点 published profile）；TUI=PTY runner；不确定或首形态失败 → escalation rerun

### ④ 双沙箱（先于②实施）
```
INSTALL/BUILD SANDBOX（跑第三方构建脚本的唯一场所）
  无 LLM/API secrets、无 K8s serviceaccount token、无 host mount、非 root、drop ALL、
  禁 RFC1918/metadata/cluster CIDR、egress 白名单（registry/GitHub 必要域）
RUNTIME SANDBOX
  临时最小凭证、独立网络策略、egress 审计
```
动机：公网可出防 SSRF 但防不住恶意 postinstall 把测试环境 API Key POST 到公网。

### ⑤ 不可逆动作人工 gate（状态机）
```
active → test-failed → needs-review →（自动）quarantine →（人工 gate）tombstone/delist/blacklist
```
- **删除「>50 条才人工」阈值**——人工介入由不可逆性决定，不由批量大小决定（误杀 1 个高星核心插件的风险可远超 200 个垃圾仓）
- 与现有谨慎删除原则同构（死链 7 天 TTL 防抖、空仓监测、跨环境证人只复核不直接改判）——是把既有思想扩展到 runtime 失败

### ⑥ Golden Sentinel Gate + run 熔断
- 固定已知结论集：known-good {npm, github, tarball, allowBuilds, web, TUI} + known-bad {missing dist, package metadata, boot crash}
- **sentinel 任意非预期 → 本轮禁止发布兼容性变化、禁止墓碑**
- run-level circuit breaker：批量状态翻转 / 安装失败率跳变 / 单一错误签名主导批次 / sentinel 不符 → 整轮 `run_suspect`，不落几百个 FAIL

## 5. 数据契约升版（RESULT_CONTRACT_REVISION → v4）

先于 ① 升版（否则改三次 runner 产生三种不可比数据）。schema 补：

```
environment: dsh_version, node_version, pnpm_version, runner_image_digest, profile, network_policy_revision
install:     resolver, resolver_snapshot_sha, install_spec, source_kind, npm_package_version,
             npm_dist_integrity, first_attempt, allow_builds_required, approved_attempt
boot:        profile, readiness_probe, timeout, verdict
function:    deterministic_verdict, model_verdict, model_id, prompt_revision
provenance:  repo_commit, package_integrity
```

顺带还历史债：README.md:259 记载的「DSH npm 版本号未随快照记录、靠 run_id 与报告日期交叉核对」——dsh_version 进 environment 后消除。

旧 1400+ 判定保留为 `legacy verdict`，**不直接映射**到新 PASS/FAIL；新契约下重测。

## 6. 实施序（评审人版，替代原 ①→②→③）

1. **⑤冻结 + ④收紧**：立即冻结自动 tombstone/delist；sandbox 收紧（安全边界不等功能改造）
2. **契约 v4 + schema**：先定证据模型
3. **①双轨 resolver**：1837 重合条目锚定站点 snapshot SHA
4. **② allowBuilds 首测/复测**：仅在 hardened build sandbox 完成后开启第二轮
5. **③ deterministic boot + L3a/L3b**
6. **⑥ Golden Sentinel + run 熔断**
7. **calibration run**：先跑双方重合 1837 条，看 divergence matrix，不急全量 6000
8. **新契约重测旧 1400+**：老结论标 legacy

## 7. 风险与开放问题

- 站点 snapshot 同步机制（拉取频率/SHA 锚定方式）待定
- web 形态判型的 manifest 特征清单需从 dsh 主线侧确认（与此前 API 面指纹讨论同源）
- calibration 后若 divergence 率异常高，先查我方环境再查站点（哨兵的裁断顺序）
- 152 迁移与本改造的交织：建议本改造直接落 152 环境（新机资源支撑双沙箱与 web 分型），旧机仅保 legacy 数据源

## 8. 兼容与迁移

- PLUGINS-ALL 渲染层：四档 → 多轴呈现（published/source/gate/boot/function 分列或折叠徽章）
- RESULT_CONTRACT_REVISION 进 input_hash：升版自动触发全量重测（现有机制，无需新代码）
- 墓碑/复活机制不变，但终局动作走 ⑤ 状态机
