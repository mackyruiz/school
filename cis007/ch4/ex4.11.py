# Ch 4 Exercise 4.11
# Macky Ruiz
# CIS 007

import sys

# Prompt the user to enter input
month = eval(input("Enter a month in the year (e.g, 1 for January: )"))
# print("month = ", month)
year = eval(input("Enter a year:"))
isLeapYear = (year % 4 == 0 and year % 100 != 0)

if month == 1:
    print("January", year, "has 31 days")
elif month == 2 and isLeapYear == True:
    print("February", year, "has 29 days")
elif month == 2 and isLeapYear == False:
    print("February", year, "has 28 days")
elif month == 3:
    print("March", year, "has 31 days")
elif month == 4:
    print("April", year, "has 30 days")
elif month == 5:
    print("May", year, "has 31 days")
elif month == 6:
    print("June", year, "has 30 days")
elif month == 7:
    print("July", year, "has 31 days")
elif month == 8:
    print("August", year, "has 31 days")
elif month == 9:
    print("September", year, "has 30 days")
elif month == 10:
    print("October", year, "has 31 days")
elif month == 11:
    print("November", year, "has 30 days")
elif month == 12:
    print("December", year, "has 31 days")
