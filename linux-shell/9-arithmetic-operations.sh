#/bin/bash

set -euo pipefail

# Task
# A mathematical expression containing +,-,*,^, / and parenthesis will be provided. 
# Read in the expression, then evaluate it. 
# Display the result rounded to decimal places.
# Sample Input 1
# 5+50*3/20 + (19*2)/7
# Sample Output 1
# 17.929


#########################
# Solition by AI actually
#########################
read -r expression

result=$(printf "%.3f" $(echo "${expression}" | bc -l))

echo  "$result"