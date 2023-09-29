#!/usr/bin/env python3

"""
Task
The provided code stub reads two integers from STDIN, a and b.
Add code to print three lines where:

  The first line contains the sum of the two numbers.
  The second line contains the difference of the two numbers (first - second).
  The third line contains the product of the two numbers.
"""

def print_operations(a, b):
    print(a+b, a-b, a*b, sep='\n')

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print_operations(a, b)
