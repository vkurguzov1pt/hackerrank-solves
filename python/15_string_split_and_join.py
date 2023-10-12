#!/usr/bin/env python3
"""
Task
You are given a string. 
Split the string on a " " (space) delimiter
and join using a - hyphen.
"""

def split_and_join(line: str) ->str:
    """
    Split incoming line, then join the parts
    Return
    """
    joined_string = '-'.join(line.split())
    return joined_string

if __name__ == '__main__':
    input_string = input()
    result = split_and_join(input_string)
    print(result)
