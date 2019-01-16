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
    matrix = random.randint(0, 1)
    return matrix

def main():
    n = eval(input("Enter n: "))
    count = 0
    while count < n:
        print(printMatrix(n), printMatrix(n), printMatrix(n))
        count +=1
main()