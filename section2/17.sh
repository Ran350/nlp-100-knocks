#!/bin/sh

echo $(cut -f 1 ./popular-names.txt | sort | uniq)
