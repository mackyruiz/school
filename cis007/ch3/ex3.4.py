# Ch2 Exercise 3.4
# Macky Ruiz
# CIS 007
import math

# Prompt the user to enter a number:
number = eval(input("Enter the side:"))

# Calculate and print
print("The area of the pentagon is", (5 * (number ** 2) / (4 * math.tan(math.pi / 5))))