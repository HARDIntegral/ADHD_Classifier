#!/bin/bash

for (( i=0; i <25; i++ ))
do
    echo "RBF KERNEL MODEL ${i}"
    python src/main.py 1
done

for (( i=0; i <25; i++ ))
do
    echo "CUSTOM KERNEL MODEL ${i}"
    python src/main.py 0
done