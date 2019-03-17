#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Run as ./check_consistency [abs_path_to_hosts_file]"
    exit 1
fi

python3.7 client/check_consistency.py $1
