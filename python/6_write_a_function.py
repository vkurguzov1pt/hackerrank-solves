#!/usr/bin/env python3

"""
Task
In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.

Given a year, determine whether it is a leap year.
If it is a leap year, return the Boolean True, otherwise return False.

"""
##############
# Solution 1 #
##############
def is_leap(year):
    leap = ''
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    return leap

##################
# Solution 2. AI #
##################
def is_leap_ai(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    year = int(input())

    print(is_leap(year))
    print(is_leap_ai(year))
