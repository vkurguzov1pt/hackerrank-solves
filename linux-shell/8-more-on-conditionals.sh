#!/usr/bin/env bash

set -euo pipefail

# Task
# Given three integers (X,Y, and Z) 
# representing the three sides of a triangle, 
# identify whether the triangle is scalene, isosceles, or equilateral.

# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.

read -r X
read -r Y
read -r Z

##########################
# Solution 1
##########################

if [ $Z -eq $Y ] && [ $Z -eq $X ] && [ $Y -eq $X ]
  then
    echo "EQUILATERAL"
    exit
fi

if [ $Z -ne $Y ] && [ $Y -ne $X ] && [ $Z -ne $X ]
  then
    echo "SCALENE"
else
  echo "ISOSCELES"
fi

##############################
### Solution 2. AI
##############################

read -r X
read -r Y
read -r Z

# Not conditional, but case
# Create a string that will help identify the triangle type
# In this example, the TYPE variable will contain a string of boolean values (1 for true, 0 for false)
TYPE=$(($X == $Y))$(($Y == $Z))$(($X == $Z))

# Check for type of triangle
case $TYPE in
    "111")
        echo "EQUILATERAL"
        ;;
    "000")
        echo "SCALENE"
        ;;
    *)
        echo "ISOSCELES"
        ;;
esac