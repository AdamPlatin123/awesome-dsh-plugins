# 插件修复与安装测试操作手册

> 适用：dsh-external-research 生态验证 · 2026-08-10
> 原则：**修复按错误类型分级**，**安装测试走真实用户路径**（marisa/dshx 或 workspace 集成），验证脚本只做报告与分类，不做有副作用的自动改码。

## 1. 错误类型 → 修复动作对照

| 错误 | 类型 | 修复动作 | 风险 |
|---|---|---|---|
| `TS2307 Cannot find module 'cordis'/'@deepseek-ai/*'` | 环境/解析 | 按插件 README 正确 workspace 集成（symlink 进 packages/tools/ + `pnpm install` 完成依赖链接）；或 marisa/dshx 安装 | 低 |
| `TS5101 baseUrl deprecated` | 配置弃用 | 插件 tsconfig 移除 `baseUrl`，paths 改相对 `./src/...` | 低（安全可自动修） |
| `TS6053/TS5083 File not found` | 路径失效 | 修正 tsconfig include/extends 相对路径 | 低 |
| `TS2688 Cannot find type definition` | 缺类型包 | `pnpm add -D @types/node`（或对应 types 包） | 低 |
| `TS2307 electron/commander/yaml 等第三方` | 依赖缺失 | `pnpm add <dep>`（插件 package.json 声明后 install） | 低 |
| `TS2339 Property does not exist` | **真实 API 漂移** | 改源码调用点（对照新 API 签名）；或升级/降级依赖版本 | **高（需人工）** |
| `TS7053/TS2412` 等（依赖源码编译错误） | 验证环境边界 | **不要修插件**——改走 project references 或真实安装验证 | — |

## 2. 修复操作流程

```bash
# 1) 定位错误
pnpm exec tsc --noEmit -p packages/tools/<插件>/tsconfig.json   # 看错误类型

# 2) 低风险自动修（配置类）
#    baseUrl 弃用：删 baseUrl 行，paths 改相对
#    缺 types：pnpm add -D @types/node
#    缺第三方依赖：pnpm add <dep>

# 3) 高风险（API 漂移）→ 人工
#    改源码调用点；改完重跑 tsc + dsh run 冒烟

# 4) 验证
bash -n scripts/*.sh                        # 脚本门
dsh run "用 <插件工具> 测试"                 # 运行级冒烟
```

## 3. 安装测试（真实用户路径，两种）

### A. marisa/dshx 安装（官方插件管理器，首选）
```bash
# 注入 marisa（一次性）
cd .clones/marisa && ./install.sh          # 拷源码到 $DSH_HOME/dshx + 软链 launcher
# 安装插件
dshx install dsh-external/<插件>            # 或从 catalog：dshx install <id>
# 验证
dshx doctor                                # 依赖/安装健康
dshx diagnostics                           # 运行时诊断
dsh run "触发插件工具"                      # 冒烟
```

### B. workspace 集成安装（源码插件）
```bash
ln -sfn $PWD/.clones/<插件> .mainline-build/packages/tools/<插件>
cd .mainline-build && pnpm install         # 链接 workspace
pnpm exec tsc --noEmit -p packages/tools/<插件>/tsconfig.json   # 编译验证
dsh run "触发插件工具"                      # 冒烟
```

### C. JS 插件（node --check 语法 + 挂载冒烟）
```bash
node --check <插件>/lib/index.js
# 挂载：cordis.yml 加相对路径插件 → dsh run 空任务观察 apply 报错
```

## 4. 已知边界（诚实声明）

1. **单包 tsc 验证有天花板**：插件 tsconfig 继承 mainline base 会把 vendor/cordis 等依赖源码拉进编译并冲突——正确验证需 **project references（tsc -b）** 或 **真实安装**（依赖用已构建 lib 类型）
2. **编译失败 ≠ 不可用**：~56% 失败仓自带 lib/ 产物可运行；~62% 是环境解析类（真实安装可解）
3. **自动修复只做低风险项**：配置/依赖类可脚本化；API 漂移类必须人工

## 5. 集成建议

- `scripts/verify-compile.sh` 报告分类（可运行/需编译/真漂移）→ 每周全量一次
- 高风险漂移（TS2339 类）→ 自动生成 issue 草稿（actions/org-issues.md）
- 低风险修复 → `scripts/fix-plugin.sh`（baseUrl 清理/依赖补装，dry-run 先出 diff）
