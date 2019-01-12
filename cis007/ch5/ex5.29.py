# Ch5 ex 5.29
# Macky Ruiz
# CIS 007
# Program prints all of the leap years in the 21st century, from 2001 to 2100.

count = 1
lineLength = 40

for count in range(2000, 2100):
        if count % 4 == 0 and count % 100 != 0:
            print(count, end=' ')
        if count % lineLength == 0:
            print()
        count += 1
