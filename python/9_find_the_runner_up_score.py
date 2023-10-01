#!/usr/bin/env python3

"""
Task
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up. 
"""

#### Solution 1 O(n*logn)
def find_runner_up_score(list_of_scores):
    """
    See the task above
    """
    return sorted(list(set(list_of_scores)))

#### Solution 2 O(n^2)
def find_runner_up_score_ai(list_of_scores):
    """
    See the task above
    """
    highest = max(list_of_scores)
    while max(list_of_scores) == highest:
        list_of_scores.remove(max(list_of_scores))
    return max(list_of_scores)

if __name__ == '__main__':
    #n = int(input())
    arr = list(map(int, input().split()))
    runner_up_score = find_runner_up_score(arr)[-2]
    runner_up_score_ai = find_runner_up_score_ai(arr)
    print(f"{runner_up_score=}")
    print(f"{runner_up_score_ai=}")
