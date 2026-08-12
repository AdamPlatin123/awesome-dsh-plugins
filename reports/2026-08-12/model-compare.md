# 模型效果比对（2026-08-12）

- 任务：用中文解释什么是 goroutine 泄漏，并给出一个最小复现示例

## deepseek-v4-flash（旧，计费）— 0 字

```
```

## Qwen3.6-35B（新，内网零费用）— 45 字

```
ERR Expecting value: line 1 column 1 (char 0)```

## 比对要点（待多模型审查）

- 正确性：两模型是否都答对核心概念
- 完整性：覆盖深度 vs 遗漏
- 代码示例：可运行性/简洁性
- 延迟：deepseek vs qwen（内网）
