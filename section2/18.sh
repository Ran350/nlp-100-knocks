#!/bin/sh

cat popular-names.txt | sort -nrk 3 | head -n 5
echo "..."
cat popular-names.txt | sort -nrk 3 | tail -n 5
