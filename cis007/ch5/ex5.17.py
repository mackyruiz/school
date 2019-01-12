# Ch5 ex5.17
# Macky Ruiz
# CIS 007

# Program that displays the characters in the ASCII character table from ! to ~. It displays ten characters per line and
# are separated by exactly one space.

count = 1
lineLength = 10                         # Create a new line after n characters

while count < 95:
    print(chr(32 + count), end = ' ')   # convert and print number to ASCII character w/one whitespace
    if count % lineLength == 0:
        print()                         # Creates new line
    count += 1
