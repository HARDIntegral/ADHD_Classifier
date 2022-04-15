#!/bin/bash

for (( i=1; i < 26; i++ ))
do
    echo "RBF KERNEL MODEL ${i}"
    python src/main.py $1
done