# Ch8 ex 8.4
# Macky Ruiz
# CIS 007

def count(word, char):
    total = 0
    for char in word:
        if char == word:
            total += 1
    return total        #Your return is inside your for loop

def main():
    word = input("Enter a string: ")
    char = input("Enter a character: ")
    print(word.count(char))
main()
