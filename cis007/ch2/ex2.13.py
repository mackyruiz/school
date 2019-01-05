# Ch2 Exercise 2.13
# Macky Ruiz
# CIS 007
# This program prompts the user to enter a four-digit integer and displays them in reverse order
# ///////////////////////////
# ex: Enter an integer: 3125
# Output:
# 5
# 2
# 1
# 3
# ///////////////////////////
#
# Prompt user for number
number = eval(input("Enter an integer: "))

# figure out each integer
d1 = number // 1000
r1 = number % 1000
d2 = r1 // 100
r2 = number % 100
d3 = r2 // 10
r3 = number % 10
d4 = r3 // 1

# Print out the number
print(d4)
print(d3)
print(d2)
print(d1)
