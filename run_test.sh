#!/bin/bash

for (( i=1; i < 51; i++ ))
do
    echo "TRIAL # ${i}"
    python3 src/main.py
done
