# Ch5 ex 7.3
# main function
# Macky Ruiz
# CIS 007
from Account import Account

def main():
    a1 = Account() #Creates an account with default values
    acc = Account(1122, 20000, 0.045)
    acc.withdraw(2500)
    acc.deposit(3000)
    print(acc.getAccountID(), acc.getBalance(), acc.getMonthlyInterestRate(), acc.getMonthlyInterest())

main()
