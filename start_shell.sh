#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Run as ./start_shell [abs_path_to_hosts_file]"
    exit 1
fi

HOSTS_PATH=$1 python3.7 client/shell.py
