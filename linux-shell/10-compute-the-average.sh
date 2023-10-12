#/usr/bin/env bash

set -euo pipefail

# Task
# Given N integers, compute their average, rounded to three decimal places.
# Sample Input
# 4
# 1
# 2
# 9
# 8
# Sample Output
# 5.000

# Read the number of integers
read N

# Initialize sum to 0
sum=0

# Loop to read integers and update sum
for (( i=0; i<N; i++ )); do
    read num
    sum=$((sum + num))
done

# Calculate and print average rounded to three decimal places
printf "%.3f\n" $(echo "$sum / $N" | bc -l)
