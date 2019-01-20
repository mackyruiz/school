# Ch9 ex 9.2
# Macky Ruiz
# CIS 007

from tkinter import * # Import tinker

class investmentCalculator:
    def __init__ (self):
        window = Tk()
        window.title("Investment Value Calculator")

        Label(window, text = "Investment Amount").grid(row = 1,
            column = 1, sticky = W)
        Label(window, text = "Years Amount").grid(row = 2,
            column = 1, sticky = W)
        Label(window, text = "Annual Interest Rate").grid(row = 3,
            column = 1, sticky = W)
        Label(window, text = "Future Value").grid(row = 4,
            column = 1, sticky = W)

        self.investmentAmountVar = StringVar()
        Entry(window, textvariable = self.investmentAmountVar,
            justify = RIGHT).grid(row = 1, column = 2)
        self.yearsVar = StringVar()

        Entry(window, textvariable = self.yearsVar,
            justify = RIGHT).grid(row = 2, column = 2)
        self.annualInterestRateVar = StringVar()

        Entry(window, textvariable = self.annualInterestRateVar,
            justify = RIGHT).grid(row = 3, column = 2)

        self.futureValueVar = StringVar()
        lblFutureValue = Label(window, textvariable =
            self.futureValueVar).grid(row = 5, column = 2, sticky = E)

        btcomputeFuture = Button(window, text = "Compute Payment",
            command = self.computeFuture).grid(
                row = 6, column = 2, sticky = E)

        window.mainloop()

    def computeFuture(self):
        investment = self.getInvestment(
            float(self.investmentAmountVar.get()),
            int(self.yearsVar.get()),
            float(self.annualInterestRateVar.get()) / 1200)
        self.futureValueVar.set(format(investment, '10.2f'))

    def getInvestment(self,
            investmentAmount, numberOfYears, monthlyInterestRate):
        investment = investmentAmount * ((1 + monthlyInterestRate) ** (numberOfYears * 12))
        return investment;

investmentCalculator()
