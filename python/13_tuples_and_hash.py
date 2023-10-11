#!/usr/bin/env python3

"""
Given an integer, n, and  n space-separated integers as input, create a tuple, t, 
of those n integers. Then compute and print the result of hash(t). 
"""

def calculate_hash(data: tuple) -> int:
    """
    Returns:
    hash value for data
    """
    return hash(data)

if __name__ == '__main__':
    n = int(input())
    integers = tuple(map(int, input().split()))
    print(calculate_hash)
