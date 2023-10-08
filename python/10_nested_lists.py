#!/usr/bin/env python3
"""
Task
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
"""

def get_second_lowest_grade(data: list) -> float:
    """
    Get second lowest score
    """
    grades = []
    for element in data:
        grades.append(element[1])

    return sorted(list(set(grades)), reverse=True)[-2]

def get_student_name(data: list, scg: float) -> list:
    """
    See the Task. scg is for second lowest score
    """

    return sorted([student[0] for student in data if student[1] == scg])

if __name__ == '__main__':
    students_and_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_and_scores.append([name,score])

    second_lowest_grade = get_second_lowest_grade(students_and_scores)
    result = get_student_name(students_and_scores, second_lowest_grade)
    print(*result, sep='\n')
