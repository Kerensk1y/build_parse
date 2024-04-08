#!/bin/bash

directory=$(find ~/ -type d -name "build_parse" | head -n 1 | tr -d '\n')

n=$(ls $directory/config/ | wc -l)


./stop.sh