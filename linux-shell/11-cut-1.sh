#!/usr/bin/env bash

# Task
# Given N lines of input, 
# print the 3rd character from each line as a new line of output. 
# It is guaranteed that each of the lines of input will have a character.

# Sample Input
# Hello
# World
# how are you

# Sample Output
# l
# r
# w

read -r N

for (( i=0; i<N; i++)); do
  read line
  echo ${line} | cut -c3
done

################################
### Solution from the public ###
################################

while read line; do
  echo $line | cut -c3
done