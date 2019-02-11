#!/bin/bash

l=$(ls | grep ^ex | grep \.py$ | wc -l)
i=$(expr $l + 1)
file=ex$i.py

if [ ! -f $file ]; then
  echo "print(\"sample ex$i\")" > $file
  python3.7 $file
  code $file
fi
