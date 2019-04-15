#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Run as ./experiment_ss_overhead [scale_factor]"
    exit 1
fi

./run_clients_distributed.sh ../odin/hosts.txt $1 6 34 NO_OP
