# Ch2 Exercise 2.15
# Macky Ruiz
# CIS 007
#
# This program prompts the user to enter the side of a hexagon and displays its area.
#
# /////////////////////////////////////////////////////
# ex: Enter the side: 5.5
# Output: The area of the hexagon is 78.59180539343781
# /////////////////////////////////////////////////////
#
#
import math

# Prompt user to enter a number
number = eval(input("Enter the side: "))

# Calculate and print
print ("The area of the hexagon is",((3 * math.sqrt(3))) / 2 * number ** 2 )
