#!/bin/bash

for (( i=1; i < 26; i++ ))
do
    echo "TRIAL # ${i}"
    python src/main.py
done