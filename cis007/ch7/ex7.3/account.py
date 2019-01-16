# Ch5 ex 7.3
# account class
# Macky Ruiz
# CIS 007


'''
UML diagram:
-----------------------------------------------------------------------------
# Class name
Account
-----------------------------------------------------------------------------
# Variable section
accountID: int
balance: float
annualInterestRate: float
-----------------------------------------------------------------------------
# Constructor
Account(accountID:int, balance:float, annualInterestRate:float)
getAccountID():int                  # accessor method
getBalance():float                  # accessor method
getAnnualInterestRate():float       # accessor method
setAccountID(accountID: int)        # mutator method
setBalance(bal:float)               # mutator method
setAnnualInterestRate(annualInterestRate:float)         # mutator method
getMonthlyInterestRate():float
getMonthlyInterest():float
deposit(ammount: float)
withdraw(ammount: float)
-----------------------------------------------------------------------------

'''

class Account:
    def __init__(self, accountID=0, balance=100, annualInterestRate=0):
        self.__accountID=accountID
        self.__balance=bal
        self._annualInterestRate=annualInterestRate
    def getAccountID(self):
        return self.__accountID

    def setAccountID(self,accoundID):
        self.__accoundID = accoundID

    def getMonthlyInterestRate(self):
        self.__aInterestRate/12

    def getMonthlyInterest(self):
        ammount = self.__balance * aInterestRate/12
        return amount
    def deposit(self, ammount):
        self.__balance += ammount
    def withdraw(self, ammount):
        self.__balance -= ammount
