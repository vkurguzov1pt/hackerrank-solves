#!/usr/bin/env python3

"""
Task
The provided code stub reads two integers from STDIN, a and b.
Add logic to print two lines. The first line should contain the result of integer division,
a//b. The second line should contain the result of float division, a/b
No rounding or formatting is necessary.
"""

def print_division_results(a, b):
    print(a//b, a/b, sep='\n')

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print_division_results(a, b)
