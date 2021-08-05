import random

print("---Welcome to Employee Wage problem---")

empCheck = random.randint(0, 1)

if empCheck == 0:
    print("\nEmployee is Absent")
elif empCheck == 1:
    print("\nEmployee is Present")

empHr = 8
empRatePerHr = 20
if empCheck == 1:
    a = empHr * empRatePerHr
    print("The Daily Wage of an Employee is", a,"\n")