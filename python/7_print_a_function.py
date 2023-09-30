#!/usr/bin/env python3

"""
Task
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following: 123...n,
i.e. n =5 => Print the string 12345
"""

def print_the_integer(input_string):
    """
    See the task above
    """
    for num in range(1, input_string + 1):
        print(num, end='')

if __name__ == '__main__':
    n = int(input())
    print_the_integer(n)
