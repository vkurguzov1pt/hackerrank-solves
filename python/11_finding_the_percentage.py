#!/usr/bin/env python3
"""
  The provided code stub will read in a dictionary containing key/value pairs
  of name:[marks] for a list of students. 
  Print the average of the marks array for the student name provided, 
  showing 2 places after the decimal. 
"""

def func(data: dict, query: str) -> float:
    """
    get the average mark for specified name aka 'query'
    """
    marks = sum(data[query])/len(data[query])

    return marks


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result_mark = func(student_marks, query_name)
    print(f"{result_mark:.2f}")
