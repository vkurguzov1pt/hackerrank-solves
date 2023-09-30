#!/usr/bin/env bash

set -euo pipefail

# Task
# Given two integers,X and Y, find their sum, difference, product, and quotient (only the integer part).
# Sample Input    Sample Output
# 5               7
# 2               3
#                 10
#                 2

read -r x
read -r y

echo "$((x + y))"
echo "$((x - y))"
echo "$((x * y))"
echo "$((x / y))"