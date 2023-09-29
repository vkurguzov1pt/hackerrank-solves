#!/usr/bin/env python3
"""
Task
The provided code stub reads and integer, n, from STDIN. 
For all non-negative integers i < n, print i^2 
"""

##################
### Solution 1 ###
##################
def return_the_squares(n):
  return [x*x for x in range(n)]

###################################
### Solution 2. Generator usage ###
###################################

def generate_the_squares(n):
  for x in range(n):
    yield x*x

if __name__ == '__main__':
  n = int(input())

  # Solution 1
  print(*return_the_squares(n), sep='\n')

  # Solution 2
  for square in generate_the_squares(n):
    print(square)
