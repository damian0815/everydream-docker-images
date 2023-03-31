#!/bin/bash
logdir=$1
port=$2

if [[ "$logdir" == "" ]]; then
    echo "Usage: $0 <logdir> [<port>]"
    exit 1
fi

if [[ "$port" == "" ]]; then
    port=8888
fi

tensorboard --logdir "$logdir" --port $port --bind_all --samples_per_plugin images=100

