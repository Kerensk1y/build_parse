#!/bin/bash

./stop.sh

nohup python3 get_response.py ; ./loop.sh
