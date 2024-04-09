#!/bin/bash

./stop.sh

python3 get_response.py &

./loop.sh