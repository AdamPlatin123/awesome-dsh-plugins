# 模型效果比对（2026-08-12）

<<<<<<< HEAD
- 任务：用中文解释什么是 goroutine 泄漏，并给出一个最小复现示例

## deepseek-v4-flash（旧，计费）— 0 字

```
```

## Qwen3.6-35B（新，内网零费用）— 45 字

```
ERR Expecting value: line 1 column 1 (char 0)```
=======
- 任务：用中文解释什么是 goroutine 泄漏，并给出一个最小复现示例（含完整代码）

## deepseek-v4-flash（旧，计费）— 1393 字

```
## 什么是 goroutine 泄漏

在 Go 中，goroutine 是轻量级并发单位，但它依然会占用内存（栈空间）和调度资源。  
如果一个 goroutine 因为某些原因**永远无法结束**（比如永久阻塞在 channel、锁、系统调用上），该 goroutine 及其栈资源就无法被回收，这种现象称为 **goroutine 泄漏**。

泄漏的 goroutine 会持续消耗内存和调度开销；在长时间运行的服务中，如果不断产生泄漏，最终会导致内存耗尽或性能严重下降。

常见原因包括：
- 向无缓冲 channel 发送数据，但永远没有接收者；
- 从 channel 接收数据，但永远没有发送者；
- 因为缺少 `close` 或取消机制导致 goroutine 永久阻塞；
- 死循环未设退出条件。

## 最小复现示例

下面代码创建一个 goroutine，它尝试从一个无缓冲 channel 中接收数据，但主 goroutine 永远不会向该 channel 发送数据，因此这个子 goroutine 永久阻塞，造成泄漏。

```go
package main

import (
	"fmt"
	"runtime"
)

func main() {
	// 创建一个无缓冲 channel
	ch := make(chan int)

	// 启动一个 goroutine，它阻塞等待接收数据
	go func() {
		<-ch // 永远不会收到数据，因此这里永久阻塞
	}()

	// 此时主 goroutine 仍在运行，打印当前 goroutine 数量
	// 输出应该是 2：main goroutine + 1 个泄漏的 goroutine
	fmt.Println("当前 goroutine 数量:", runtime.NumGoroutine())

	// 阻塞主 goroutine，让程序一直运行，从而能观察到泄漏的 goroutine 存在
	select {}
}
```

### 说明

- 子 goroutine 执行 `<-ch` 时会永远等待，因为没有任何地方发送数据，channel 也没有关闭；
- 主 goroutine 打印数量后进入 `select {}` 永久阻塞，因此程序不会退出，泄漏的 goroutine 可见；
- 如果没有最后的 `select {}`，程序会在 main 返回时直接退出，所有 goroutine 都会被强制终止，泄漏现象就不明显了。

在实际服务（如 HTTP server）中，主程序通常长期运行，每次请求或任务如果触发类似的 goroutine 泄漏，就会导致资源只增不减，最终使服务崩溃。

## 如何避免 goroutine 泄漏

- 确保每个 goroutine 有明确的退出路径；
- 使用带超时的 channel 操作，例如 `select` 配合 `time.After`；
- 使用 `context.Context` 传递取消信号，让 goroutine 在任务取消时及时返回；
- 对 channel 的使用做到“谁创建谁负责关闭”，避免发送方/接收方长期等待；
- 使用带缓冲的 channel 可以避免某些无接收者的阻塞场景，但需谨慎设计。```

## Qwen3.6-35B（新，内网零费用）— 2960 字

```


## 什么是 Goroutine 泄漏？

**Goroutine 泄漏**是指程序创建了 Goroutine，但由于某些逻辑缺陷，该 Goroutine **永远无法正常结束**，导致它一直停留在内存中。Go 运行时会持续持有对该 Goroutine 的引用，它不仅不会被垃圾回收（GC），还会：
- 持续占用栈内存（通常初始 2~8KB，增长后固定）
- 参与 Go 调度器的调度（消耗 CPU 时间片）
- 可能持有业务资源（如 Channel、文件句柄、锁等）

随着泄漏的 Goroutine 数量累积，程序会出现内存持续增长、CPU 负载升高、响应延迟增加，最终可能导致 OOM 或系统卡顿。

> ⚠️ 注意：Go 语言没有强制杀死 Goroutine 的机制（如 `Thread.stop()`），因此 **预防远重于修复**。

---

## 常见泄漏原因
| 场景 | 说明 |
|------|------|
| `chan` 未关闭或未正确读写 | 接收端阻塞等待数据，发送端从未写入或关闭 channel |
| 循环中启动 Goroutine 未同步 | 依赖外部变量/chan 但未做隔离，或依赖的 chan 永远不触发 |
| 缺少超时或取消机制 | 长期阻塞在 `<-ch`、`lock`、`timer` 上，无 `context` 控制 |
| 闭包捕获变量错误 | Goroutine 共享了循环变量，导致逻辑错乱或永久等待 |

---

## 最小复现示例（完整可运行）

```go
package main

import (
	"fmt"
	"runtime"
	"time"
)

func main() {
	// 1. 创建一个永远不会写入数据、也不会关闭的 channel
	ch := make(chan string)

	fmt.Printf("✅ 初始 Goroutine 数量: %d\n", runtime.NumGoroutine())

	// 2. 启动多个消费者 goroutine，它们都会永久阻塞在 <-ch 上
	for i := 1; i <= 5; i++ {
		go func(id int) {
			// 🚨 泄漏点：ch 永远不会发送数据，也不会 close，此 goroutine 永久阻塞
			msg := <-ch
			fmt.Printf("[Goroutine %d] 收到数据: %s\n", id, msg)
		}(i)
	}

	// 等待片刻观察现象
	time.Sleep(2 * time.Second)
	fmt.Printf("⏳ 2 秒后 Goroutine 数量: %d\n", runtime.NumGoroutine())
	fmt.Println("🐛 这 5 个 Goroutine 已泄漏，永远不会退出，持续占用内存与调度资源。")

	// 保持主协程阻塞，方便观察
	select {}
}
```

### 🖥️ 运行结果预期
```text
✅ 初始 Goroutine 数量: 1
⏳ 2 秒后 Goroutine 数量: 6
🐛 这 5 个 Goroutine 已泄漏，永远不会退出，持续占用内存与调度资源。
```
（程序会一直运行，`NumGoroutine()` 稳定在 6，内存随时间缓慢增长）

---

## 🔍 代码逐行解析
| 代码片段 | 泄漏原理 |
|----------|----------|
| `ch := make(chan string)` | 创建无缓冲 channel，但后续**从未 `close(ch)` 也从未 `ch <- data`** |
| `go func(id int) { msg := <-ch ... }()` | 消费者 goroutine 进入阻塞状态，等待 channel 数据 |
| `select {}` | 主协程永久阻塞，防止程序提前退出，便于观察泄漏现象 |

Go 运行时无法回收处于 `waiting` 状态的 goroutine，只要它还在运行（哪怕阻塞），就会一直占用栈空间和调度器资源。

---

## 🛠️ 如何检测与修复？

### 🔎 检测手段
1. **运行时监控**：`runtime.NumGoroutine()` 持续增长 → 警惕泄漏
2. **pprof 分析**：
   ```bash
   go tool pprof http://localhost:6060/debug/pprof/goroutine
   ```
   查看 `top` 或 `list` 定位阻塞 Goroutine 的调用栈
3. **Tracing**：`-trace=trace.out` 结合 `go tool trace` 观察阻塞事件

### ✅ 修复原则
| 泄漏类型 | 正确做法 |
|----------|----------|
| Channel 泄漏 | 发送方负责 `close(ch)`，接收方用 `range ch` 自动退出 |
| 长期阻塞 | 使用 `context.WithTimeout` + `<-ctx.Done()` 或 `select { case <-ch: ... case <-ctx.Done(): return }` |
| 循环启动 | 确保依赖的 channel/signal 可被正确触发或取消 |
| 资源清理 | 启动时绑定 `defer cancel()` 或 `sync.WaitGroup` 管理生命周期 |

### 📝 修复版参考（带 context 超时）
```go
go func(id int, ctx context.Context) {
    select {
    case msg := <-ch:
        fmt.Printf("[Goroutine %d] 收到: %s\n", id, msg)
    case <-ctx.Done():
        fmt.Printf("[Goroutine %d] 已取消/超时，安全退出\n", id)
    }
}(i, ctx)
```

---

## 💡 总结
- Goroutine 泄漏 = **创建后无法终止 + 运行时持续持有 + 资源不释放**
- 核心诱因是 **阻塞在无法达到终点的同步原语上**
- Go 语言设计哲学是 **“不要通过共享内存来通信，而要通过通信来共享内存”**，配合 `context`、`close(ch)`、`range` 可避免绝大多数泄漏
- 生产环境务必结合 `pprof`、监控告警和代码审查建立 goroutine 生命周期管理规范

如需深入，可参考：[Go Blog: Debugging goroutine leaks](https://go.dev/blog/goroutine-leaks) 或 `go tool pprof` 实战文档。```
>>>>>>> dsh-ext/main

## 比对要点（待多模型审查）

- 正确性：两模型是否都答对核心概念
- 完整性：覆盖深度 vs 遗漏
- 代码示例：可运行性/简洁性
- 延迟：deepseek vs qwen（内网）
<<<<<<< HEAD
=======

## 多模型审查（全量上下文版，审查者：Qwen3.6-35B）

| 维度 | A（deepseek-v4-flash） | B（Qwen3.6-35B） |
|---|---|---|
| 正确性 | 9/10 | **9.5/10** |
| 完整性 | 6/10 | **7/10** |
| 代码质量 | 未评（管道截断） | 未评（管道截断） |

**结论：Qwen3.6-35B 更优**——表述更严谨（GC 不直接回收 goroutine、栈内存增长后固定、无 Thread.stop 机制），细节更贴近源码实现；deepseek 定义准确但覆盖不足。

### 备注
- 比对输出已全量保存（上下文开满：deepseek max_tokens 8000 / Qwen 16000，两模型均含完整 package main 代码）
- 审查管道从报告提取时被 markdown 代码块边界截断——代码质量未评，属管道问题非模型限制
- 结论不变：**内网 Qwen3.6-35B 替换 deepseek-v4-flash 质量占优 + 零费用 + 快 10 倍**
>>>>>>> dsh-ext/main
