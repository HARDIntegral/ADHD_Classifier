#!/usr/bin/env bash

root=$(dirname $0)

cd "${root}/../"

python3 Source/Generate/Generate.py

cd -