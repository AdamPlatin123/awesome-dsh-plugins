# 对端服务器模型消耗报告（2026-08-12）

## 远程 omp 订阅额度

- 状态：⚠️ 远程 agent.db 损坏/不可读（DB_CORRUPT *** in database main ***）


## 监控链自身模型消耗

- dsh run 冒烟痕迹：0 轮日志含
- 最近构建：[构建] 完成 rc=install:0 build:0 耗时 23s
- 说明：cron 全链路为纯脚本（0 LLM token）；模型消耗仅来自手动 dsh 冒烟测试

## 备注

- 远程 omp 订阅（GLM/DeepSeek）有效期至 2026-09-01；额度消耗以 provider 侧账单为准
- agent.db usage_history 损坏时无法读取历史趋势，需 omp 侧修复（omp 不运行时 .recover）
