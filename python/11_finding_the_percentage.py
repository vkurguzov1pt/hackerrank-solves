#!/usr/bin/env python3
"""
  The provided code stub will read in a dictionary containing key/value pairs
  of name:[marks] for a list of students. 
  Print the average of the marks array for the student name provided, 
  showing 2 places after the decimal. 
"""

def func(data: dict, query: str) -> float:
    """
    data (dict): a dict containing student names - keys and marks - values
    query (str): the name of a student whose avg marks is calculated

    Returns:
    float: the avg mark for the specified student
    """
    avg_mark = sum(data[query])/len(data[query])

    return avg_mark


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
