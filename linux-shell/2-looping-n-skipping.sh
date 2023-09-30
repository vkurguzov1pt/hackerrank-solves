#!/usr/bin/env bash

# """
# Task
# Your task is to use for loops to display only odd natural numbers from 1 to 99
# """

set -euo pipefail

##################
# Solution 1
##################
seq 1 2 99

####################
# Solution 2 AI
####################

for num in {1..99..2}
do
   echo $num
done