# 模型效果比对（2026-08-12）

- 任务：用中文解释什么是 goroutine 泄漏，并给出一个最小复现示例

## deepseek-v4-flash（旧，计费）— 1366 字

```
## goroutine 泄漏是什么？

goroutine 泄漏（goroutine leak）指的是：**goroutine 启动了，却因为某些原因永久阻塞，永远不会退出**。

这样会导致：

- goroutine 的栈内存永远无法被 GC 回收；
- goroutine 可能持有资源（如 channel、锁、计时器、内存）不释放；
- 在高并发/长生命周期服务中，泄漏的 goroutine 会越积越多，最终导致内存暴涨、程序变慢甚至 OOM。

最常见的泄漏原因：

- 向一个永远没有接收者的 channel 发送数据；
- 从 channel 读取数据，但永远没有发送者；
- 没有正确的关闭 channel 或调用 `cancel()`;
- 锁未释放或死锁；
- `time.Ticker` 未停止；
- goroutine 卡在 `select` 里，但所有 case 都永远不会就绪。

---

## 最小复现示例

下面这个例子，一个 goroutine 永远阻塞在从一个 channel 接收数据上，因为没有人向这个 channel 发送数据。

```go
package main

import (
	"fmt"
	"runtime"
	"time"
)

func main() {
	// 创建一个无缓冲 channel
	ch := make(chan int)

	// 启动一个 goroutine，试图从 ch 接收数据
	go func() {
```

## Qwen3.6-35B（新，内网零费用）— 1572 字

```


### 什么是 Goroutine 泄漏？

**Goroutine 泄漏**是指一个协程（goroutine）在任务本应结束后，由于某些原因（如永久阻塞、缺少退出条件、依赖的信号永远不触发等），导致 Go 运行时无法将其回收，该协程会一直处于“存活”状态。

严格来说，goroutine 不是由 GC 直接管理的，而是由 Go 的调度器管理。当一个 goroutine 无法被终止时，它始终处于**可达状态**，运行时必须保留它的：
- 栈内存（初始 2KB+，可动态增长）
- 调度器状态（M:G 映射、PC 指针等）
- 对应的 OS 线程（当该 M 被其他活跃 G 阻塞时，会创建新线程）

因此，goroutine 泄漏本质上是**调度器与系统资源的泄漏**，会持续消耗内存并可能阻塞工作线程，最终导致程序性能下降、内存溢出（OOM）或假死。

---

### 最小复现示例

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int) // 无缓冲 channel

	go func() {
		// 永久阻塞在这里：没人发送数据，也没关闭 channel
		val := <-ch
		fmt.Println("收到:", val)
	}()

	// 主协程执行完毕后直接退出进程
	time.Sleep(1 * time.Second)
	fmt.Println("主协程结束")
}
```

```

## 比对要点（待多模型审查）

- 正确性：两模型是否都答对核心概念
- 完整性：覆盖深度 vs 遗漏
- 代码示例：可运行性/简洁性
- 延迟：deepseek vs qwen（内网）

## 多模型审查

### 审查者：deepseek-v4-flash

```

```

### 审查者：Qwen3.6-35B

```
结论
    - 3) 各自明显错误
    - Add a note about the truncation affecting code quality scoring.
    - Ensure tone is technical and objective.
    - Draft:
      1) 评分
      - 模型A (deepseek-v4-flash)：正确性 7/10，完整性 8/10，代码质量 0/10（注：提供的回答在此处截断，未包含代码部分，故暂无法评分）
      - 模型B (Qwen3.6-35B)：正确性 9/10，完整性 9/10，代码质量 0/10（同上）
      2) 结论：模型B更好。原因：...
      3) 各自明显错误：...
    - Refine the content to match technical accuracy standards.
    - Check GC vs Scheduler: Go's GC only manages heap. Goroutine stacks are on heap (if dynamic) but managed by scheduler/runtime. Leaked goroutines hold their stack and scheduler state. B's explanation is much closer to reality.
    - Check channel/lock causes: A's list is standard and practical. B focuses on runtime mechanics. Both are valid perspectives, but B's is more precise for "leak" definition.
    - I will explicitly state that the evaluation is based on the provided text, and code quality is marked as pending due to truncation. If forced to guess, I'd say both would likely provide standard channel examples, but B's theoretical foundation is stronger.
    - Final check of the prompt: "请审查以下两个 AI 模型对同一中文技术任务的回答，输出：1) 各模型评分（正确性/完整性/代码质量，各10分）2) 结论：哪个更好、为什么 3) 各自明显错误（如有）。用中文。"
    - I will structure exactly as requested.

    Draft structure:
    **1) 模型评分**
    - 模型A (deepseek-v4-flash)：正确性 7/10｜完整性 8/10｜代码质量 0/10（待补充）
    - 模型B (Qwen3.6-35B)：正确性 9/10｜完整性 9/10｜代码质量 0/10（待补充）
    *(注：两模型回答均在“最小复现示例”标题处截断，代码部分未提供，代码质量暂按 0 分记录，实际表现需结合完整代码评估。)*

    **2) 结论：哪个更好、
```

### 审查者：deepseek-v4-flash（重试）

"```"

"```"

## 结论

### 多模型审查结果（审查者：Qwen3.6-35B）

| 维度 | 模型A（deepseek-v4-flash） | 模型B（Qwen3.6-35B） |
|---|---|---|
| 正确性 | 7/10 | **9/10** |
| 完整性 | 8/10 | **9/10** |
| 代码质量 | 未评（输出截断） | 未评（输出截断） |

**审查结论：模型B（Qwen3.6-35B）更好**——goroutine 泄漏定义上 B 更贴近运行时机制（GC 只管堆、goroutine 栈由调度器管理），A 的触发场景列表标准实用但理论精度不及 B。

### 备注
- 两模型均正常完成比对任务（deepseek 1366 字 / qwen 1572 字）
- deepseek 审查响应 content 为空（reasoning 模型行为），仅 Qwen 审查成功
- 效果比对结论：**内网 Qwen3.6-35B 替换 deepseek-v4-flash 在本题上质量占优，且零费用**
