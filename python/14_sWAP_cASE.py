#!/usr/bin/env python3
"""
Task
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Input: HackerRank.com presents "Pythonist 2".
Output hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""

def swap_one_by_one(s: str) -> str:
    """
    Change
    Returns: string with changed case
    """
    modified_str = s.lower() if s.isupper() else s.upper()

    return modified_str

def swap_case(input_string: str) -> str:
    """
    Returns:
    the modified string
    """
    swapped_string = ''.join(map(swap_one_by_one,input_string))

    return swapped_string


if __name__ == '__main__':
    string_to_swap_case = input()
    RESULT = swap_case(string_to_swap_case)
    print(RESULT)
