import random

print("---Welcome to Employee Wage problem---")

empCheck = random.randint(0, 1)

if empCheck == 0:
    print("Employee is Absent")
elif empCheck == 1:
    print("Employee is Present")