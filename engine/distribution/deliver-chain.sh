#!/usr/bin/env bash
# 等 finish-rerun.sh 进程退出（它自己会聚合+推个人仓库），然后 bot PR 交付到 awesome-dsh-plugins
while pgrep -f "bash ~/dsh-k8s/finish-rerun.sh|bash /home/adam/dsh-k8s/finish-rerun.sh" >/dev/null 2>&1; do sleep 60; done
sleep 5
bash ~/dsh-k8s/bot-deliver.sh
