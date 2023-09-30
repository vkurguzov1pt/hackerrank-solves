#!/usr/bin/env bash


# Task
# Use a for loop to display the natural numbers from 1 to 50.
#

# Both variants are possible
for number in $(seq 1 50)
do
  echo $number
done

for number in {1..50}; do
  echo $number
done