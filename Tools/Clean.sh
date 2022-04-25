#!/usr/bin/env bash

root=$(dirname $0)
library="${root}/../Source/SVM"

cd $library

make clean

cd -