#!/bin/sh

IN_FILE="./popular-names.txt"
len_line=$(cat $IN_FILE | wc -l)
skip=$(expr $len_line / $1)

# skip 行ずつ分割する
split -dl $skip --additional-suffix=".txt" $IN_FILE popular-names
