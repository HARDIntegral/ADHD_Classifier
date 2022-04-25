#!/usr/bin/env bash

root=$(dirname $0)
# makefile="${root}/../Source"

cd "${root}/../Source/SVM"

make $1

cd -