#!/usr/bin/env bash

set -euo pipefail

# Task
# Read in one character from STDIN.
# If the character is 'Y' or 'y' display "YES".
# If the character is 'N' or 'n' display "NO".
# No other character will be provided as input.


read -r P
if [ $P == "Y" ] || [ $P == "y" ]
  then
    echo "YES"
else
    echo "NO"
fi

      