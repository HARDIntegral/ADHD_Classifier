#!/usr/bin/env bash

root=$(dirname $0)
main="${root}/../Source/main.py"

for (( i=1; i < 251; i++ ))
do
    echo "TRIAL # ${i}"
    python3 "$main"
done
