#!/usr/bin/env python3

"""
Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20 , print Weird
If n is even and greater than 20, print Not Weird
"""

import math
import os
import random
import re
import sys

#################
# My Solution
#################

def what_is_n(n):
    message = ''
    if n % 2 != 0:
        message = "Weird"
    elif n % 2 == 0 and n in range(2,6):
        message = "Not Weird"
    elif n % 2 == 0 and n in range(6,21):
        message = "Weird"
    elif n % 2 == 0 and n > 20:
        message = "Not Weird"

    return message
      

if __name__ == '__main__':
    n = int(input().strip())
    result = what_is_n(n)
    print(result)