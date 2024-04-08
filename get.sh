#!/bin/bash

while True; then
	python3 get_response.py &
	get_pid=$!
	sleep(260000)
	kill $get_pid
done
