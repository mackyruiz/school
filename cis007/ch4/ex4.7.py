# Ch4 ex 4.7
# Macky Ruiz
# CIS 007

# Receive the amount
amount = eval(input("Enter an amount in double, e.g., 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = int(remainingAmount / 100)
remainingAmount = int(remainingAmount % 100)

# Find the number of quarters in the remaining amount
numberOfQuarters = int(remainingAmount / 25)
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = int(remainingAmount / 10)
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = int(remainingAmount / 5)
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display results
print("Your amount", amount, "consists of")
if numberOfOneDollars == 1:
    print("\t", numberOfOneDollars, "dollar")
elif numberOfOneDollars >= 2:
    print("\t", numberOfOneDollars, "dollars")
if numberOfQuarters == 1:
    print("\t", numberOfQuarters, "quarter")
elif numberOfQuarters >= 2:
    print("\t", numberOfQuarters, "quarters")
if numberOfDimes == 1:
    print("\t", numberOfDimes,  "dime")
elif numberOfDimes >= 2:
    print("\t", numberOfDimes,  "dimes")
if numberOfNickels == 1:
    print("\t", numberOfNickels, "nickel")
elif numberOfNickels >= 2:
    print("\t", numberOfNickels, "nickels")
if numberOfPennies == 1:
    print("\t", numberOfPennies, "penny")
elif numberOfPennies >= 2:
    print("\t", numberOfPennies, "pennies")
