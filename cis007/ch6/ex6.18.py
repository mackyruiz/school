# Ch5 ex 6.18
# Macky Ruiz
# CIS 007

# Display matrix of 0s and 1s. Write a function that displays an n-by-n matrix. Prompt the user to enter n and displays
# an n-by-n matrix. sample:
# Enter n: 3
# 0 1 0
# 0 0 0
# 1 1 1
import random
def printMatrix(number):
    number = 0
    if number < 1:
        matrix = random.randint(0, 1)

def main():
    n = eval(input("Enter n: "))
    printMatrix(n)