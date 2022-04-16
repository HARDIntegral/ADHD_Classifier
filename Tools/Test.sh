#!/usr/bin/env bash

root=$(dirname $0)
main="${root}/../src/main.py"

for (( i=1; i < 51; i++ ))
do
    echo "TRIAL # ${i}"
    python3 "$main"
done
