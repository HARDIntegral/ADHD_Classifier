#!/bin/bash

for (( i=1; i < 26; i++ ))
do
    echo "CUSTOM KERNEL MODEL ${i}"
    python src/main.py $1
done