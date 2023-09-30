#!/usr/bin/env bash

set -euo pipefail

# """
# Task:
# Write a Bash script which accepts as input and displays the greeting "Welcome (name)"
# """

read -p 'Name: ' name
echo "Welcome, ${name}"