# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by:
# @Last Modified time:
# @Title : Employee Wage
# '''

import random

print("---Welcome to Employee Wage problem---")

EMP_FULL_HR = 16
EMP_HALF_HR = 8
EMP_RATE_PER_HR = 20
NUM_OF_WORKING_DAYS = 20

"""
Description:
    created function for each condition and called in switcher.
Parameter:
    for full day hours is 16 hr. for half day hours is 8 hrs. and for absent 0 hours.
Return:
    Returning the value of full day hour, half day hour and some time 0 hrs.
"""

def absent():
    return 0

def full_day():
    return 16

def half_day():
    return 8

def check_attendance(i):
    switcher = {
        0: absent,
        1: full_day,
        2: half_day
    }
    return switcher.get(i, "nothing")()


def calculate_wage():
    i = 0
    j = 0
    while i <= 100 and j < 21:
        j += 1
        emp_Check = random.randint(0, 2)
        i += check_attendance(emp_Check)
    print(i)

    print("Employee Monthly Wage for 100 hrs is:",i * 20)

if __name__== '__main__':
    calculate_wage()