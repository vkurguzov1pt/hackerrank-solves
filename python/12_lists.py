#!/usr/bin/env python3

"""
Task
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer at position
print: Print the list.
remove e: Delete the first occurrence of integer
append e: Insert integer at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value n of followed by n lines of commands,
where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list

Example
N = 4
append 1
append 2
insert 3 1
print
"""

def func(data: list):
    """
    sss
    """
    result = []
    for elem in data:
        if elem[0] == 'print':
            print(result)
        else:
            getattr(result, elem[0])(*elem[1])
    return result

if __name__ == '__main__':
    n = int(input())
    inputs = []
    for _ in range(n):
        method, *arg = input().split()
        args = list(map(int, arg))
        inputs.append([method,args])
    func(inputs)
