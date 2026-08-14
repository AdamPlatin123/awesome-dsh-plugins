#!/usr/bin/env python3
"""de-stream proxy: dsh(stream=True) -> Qwen(stream=False) -> 单 SSE 块回传.

解决的问题（定位过程见 README）：vLLM 在 **stream=True** 时，tool_call chunk 的 `name`
字段是 null；stream=False 时 name 完整。本代理把 dsh 的流式请求转成非流式发给 Qwen，
拿到完整 tool_calls 后重包成单个 SSE chunk 回给 dsh——dsh 拿到正确的工具名。

同时：
- max_tokens 抬到 8192（Qwen3.6 会先 reasoning 再 tool_call，预算不足会吐空 name）。
- parallel_tool_calls=false（Qwen 并行 tool call 经重包会丢 per-call index → 参数拼接 → 400）。

上游 Qwen 地址走环境变量 QWEN_BASE_URL，默认占位（部署时注入，勿硬编码内网地址到公开仓库）。
"""
import http.server, urllib.request, json, os, sys

UP = os.environ.get("QWEN_BASE_URL", "http://QWEN_HOST:8080")


class H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        L = int(self.headers.get("content-length", 0))
        body = self.rfile.read(L)
        try:
            d = json.loads(body)
            d["max_tokens"] = 8192
            d["stream"] = False
            d["parallel_tool_calls"] = False
            d.pop("stream_options", None)
        except Exception as e:
            sys.stderr.write("parse err %s\n" % e)

        req = urllib.request.Request(UP + self.path, data=json.dumps(d).encode(),
                                     headers={"content-type": "application/json"}, method="POST")
        try:
            r = urllib.request.urlopen(req, timeout=300)
            o = json.loads(r.read())
            m = o["choices"][0].get("message", {})
            fr = o["choices"][0].get("finish_reason") or "stop"
            delta = {"role": "assistant"}
            if m.get("content"):
                delta["content"] = m["content"]
            if m.get("tool_calls"):
                delta["tool_calls"] = m["tool_calls"]
            chunk = {"id": o.get("id", "x"), "object": "chat.completion.chunk",
                     "created": o.get("created", 0), "model": o.get("model", ""),
                     "choices": [{"index": 0, "delta": delta, "finish_reason": None}]}
            final = {"id": o.get("id", "x"), "object": "chat.completion.chunk",
                     "created": o.get("created", 0), "model": o.get("model", ""),
                     "choices": [{"index": 0, "delta": {}, "finish_reason": fr}]}
            names = [c.get("function", {}).get("name") for c in (m.get("tool_calls") or [])]
            sys.stderr.write("de-stream OK fr=%s names=%s\n" % (fr, names))
            self.send_response(200)
            self.send_header("content-type", "text/event-stream")
            self.send_header("cache-control", "no-cache")
            self.end_headers()
            self.wfile.write(("data: " + json.dumps(chunk) + "\n\n").encode())
            self.wfile.write(("data: " + json.dumps(final) + "\n\n").encode())
            self.wfile.write(b"data: [DONE]\n\n")
            self.wfile.flush()
        except urllib.error.HTTPError as e:
            sys.stderr.write("fwd err HTTP %d: %s\n" % (e.code, e.read().decode()[:200]))
            self.send_response(502); self.end_headers(); self.wfile.write(b"proxy upstream error")
        except Exception as e:
            sys.stderr.write("fwd err %s\n" % str(e)[:200])
            self.send_response(502); self.end_headers(); self.wfile.write(str(e).encode())

    def do_GET(self):
        self.send_response(200); self.send_header("content-type", "application/json"); self.end_headers()
        self.wfile.write(b"{\"object\":\"list\",\"data\":[{\"id\":\"Qwen3.6-35B\"}]}")

    def log_message(self, *a):
        pass


http.server.HTTPServer(("0.0.0.0", 18093), H).serve_forever()
