# dsh-test-runner: 容器内 dsh（agent）+ Qwen 驱动的插件运行级测试
#
# agent 读插件 README → 自主导入 dsh → 验证；全程经本地 de-stream 代理用 Qwen。
# Qwen 上游地址走运行时环境变量 QWEN_BASE_URL（见 job.yaml），勿硬编码内网地址。
FROM node:22-slim

# 运行时 + node-pty 等 native 模块的 node-gyp 编译依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl ca-certificates build-essential python3 \
    && rm -rf /var/lib/apt/lists/*

# dsh（被测目标 + agent 框架，原生支持 OpenAI 兼容的 Qwen）
RUN npm install -g @deepseek-ai/dsh@0.1.0-rc.6

# de-stream 代理（修 vLLM 流式 tool_call name=null 的 bug）+ 测试脚本
COPY destream-proxy.py test-plugin-agent.sh shard-runner.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/destream-proxy.py /usr/local/bin/test-plugin-agent.sh /usr/local/bin/shard-runner.sh

# 非 root（Claude-Code 式 agent 拒绝 root；复用 node 用户 uid 1000 与宿主对齐以便 hostPath 写）
USER node
ENV HOME=/home/node \
    DEEPSEEK_API_KEY=none
WORKDIR /home/node/work
CMD ["shard-runner.sh"]
