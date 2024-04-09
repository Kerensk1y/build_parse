#!/bin/bash

directory=$(find ~/ -type d -name "build_parse" | head -n 1 | tr -d '\n')

n=$(ls config/ | wc -l)

./stop.sh

if [-f added.txt]; then
	for i in $(seq 1 $n); do
		first=$($n-$i+1)
		second=$($first+1)
		mv config/$first.txt config/$second.txt
done

mv added.txt config/1.txt

./loop.sh
