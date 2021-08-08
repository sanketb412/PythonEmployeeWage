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

def absent():
    return "Employee is Absent"

def full_day():
    return "Employee Present full day and daily wage is",EMP_FULL_HR*EMP_RATE_PER_HR

def half_day():
    return "Employee Present half day and daily wage is",EMP_HALF_HR*EMP_RATE_PER_HR

def check_attendance(i):
    switcher = {
        0: absent,
        1: full_day,
        2: half_day
    }
    return switcher.get(i, "nothing")() 

for i in range (1, 21):
    emp_Check = random.randint(0, 2)
    print(check_attendance(emp_Check))