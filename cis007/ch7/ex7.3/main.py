# Ch5 ex 7.3
# main function
# Macky Ruiz
# CIS 007
from account import Account

def main():
    a1 = account() #Creates an account with default values
    acc = account(1122, 20000, 0.045)
    acc.withdraw(2500)
    acc.deposit(3000)
    print(acc.getAccountID(), acc.getBalance(), getMonthlyInterestRate(), acc.getMonthlyInterest())

main()
