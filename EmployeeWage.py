# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by:
# @Last Modified time:
# @Title : Employee Wage
# '''

import random

print("---Welcome to Employee Wage problem---")

empCheck = random.randint(0, 2)

is_Full_Day = 1
is_Half_Day = 2
empHr = 16
empHrHalf = 8
empRatePerHr = 20

if empCheck == is_Full_Day:
    print("\nEmployee is Present Full day \nEmployee Daily Wage in Rupees is:", empHr*empRatePerHr,"\n")
elif empCheck == is_Half_Day:
    print("\nEmployee is Present Half day \nEmployee Daily Wage in Rupees is:", empHrHalf*empRatePerHr,"\n")
else:
    print("\nEmployee is Absent\n")
