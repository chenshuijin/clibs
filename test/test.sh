#!/bin/bash

for f in `find . -name "*.py"`
do
    echo "=================run $f==============="
    $f
done
