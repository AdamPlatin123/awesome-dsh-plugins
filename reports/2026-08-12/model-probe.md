# 模型真实上限实测（2026-08-12，纯 python 探测，服务端实际响应为准）

## 输出上限（max_tokens 请求 vs 实际 completion）

| 请求 max_tokens | deepseek-v4-flash | Qwen3.6-35B |
|---|---|---|
| 100 | 100（length） | 100（length） |
| 2000 | 2000（length） | 397（stop） |
| 8192 | 6583（stop） | 1230（stop） |
| 16000 | 6290（stop） | 2029（stop） |
| 32768 | 12357（stop） | 5430（stop） |
| 64000 | **56239（stop）** | 2673（stop） |

**结论**：
- deepseek-v4-flash 输出上限 ≈ **56K tokens**（64000 请求产出 56239；32000 时 12K 是模型自停）
- Qwen3.6-35B 输出上限 ≈ **2.7-5.4K tokens**（reasoning 消耗后 stop；请求再大也停在 ~5.4K 内）

## 输入上限（递增输入，total_tokens 实测）

| 输入大小 | deepseek-v4-flash | Qwen3.6-35B |
|---|---|---|
| 8K 字 | OK（4425） | — |
| 32K 字 | OK（17436） | — |
| 64K 字 | OK（34784） | OK（34711） |
| 128K 字 | OK（69479） | OK（69406） |
| 256K 字 | OK（138870） | OK（138797） |
| 512K 字 | OK（277653） | **400：maximum context length is 262144 tokens** |

**结论**：
- deepseek-v4-flash 输入上限 **≥ 512K 字（27.7 万 token，未触顶）**
- Qwen3.6-35B 输入上限 = **262144 tokens**（服务端报错确认，与 vLLM max_model_len 声明一致）

## 对配置的意义

- qwen-local 配置 contextWindow=262144 ✓ 准确；maxTokens=16384 超出其实际输出能力（服务端 stop 无害，可调低至 8192）
- 长输出任务（大代码/长文档生成）**Qwen 不适合**（≤5.4K），deepseek-v4-flash 可到 56K——按任务类型选择模型
