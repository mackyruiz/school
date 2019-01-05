# Ch2 Exercise 2.5
# Macky Ruiz
# CIS 007
# This program reads the subtotal and the gratuity rate, then computes the gratuity and total
#
# /////////////////////////////////////////////////////////////
# ex: subtotal = 16.20, gratuity = 20
# Enter The subtotal and a gratuity rate: 16.20, 20
# Output:
# The gratuity is 3.24 and the total is 19.439999999999998
# ////////////////////////////////////////////////////////////
#
#Prompt the user for input
subtotal, gratuity = eval(input("Enter The subtotal and a gratuity rate: "))

#calculate tip
tip = (gratuity / 100) * subtotal

# Compute sales tax
total = subtotal + tip

print("The gratuity is", tip, "and the total is", total)
