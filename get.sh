#!/bin/bash

directory=$(find ~/ -type d -name "build_parse" | head -n 1 | tr -d '\n')

while [-n $directory]; then
	python3 $directory/get_response.py
	sleep(260000)
	py_pid=$(pgrep -f "python3 $directory/get_response.py")
	kill $py_pid
done
