# Ch2 Exercise 3.9
# Macky Ruiz
# CIS 007

# Take user inputs
name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
rate = eval(input("Enter hourly pay rate: "))
FedTax = eval(input("Enter federal tax withholding rate: "))
StateTax = eval(input("Enter state tax withholding rate: "))

# Calculate pay and deductions
# Total pay before taxes
GrossPay = hours * rate

# Federal taxes based on gross pay
FedWithholding = FedTax * GrossPay

# State taxes based on gross pay
StateWithholding = StateTax * GrossPay

# Total tax deductions
TaxDeductions = FedWithholding + StateWithholding

# Total after taxes
NetPay = GrossPay - TaxDeductions

# Print calculated data based on user input
print("\n",
      "Employee Name:", name, "\n",
      "Hours Worked: {:,.1f}".format(hours), "\n",
      "Hourly Rate: ${:,.2f}".format(rate), "\n",
      "Gross pay: ${:,.2f}".format(GrossPay), "\n",
      "Deductions: \n",
      "\t", "Federal Withholding ({:,.1%}):".format(FedTax), "${:,.2f}".format(FedWithholding), "\n",
      "\t", "State Withholding ({:,.1%}):".format(StateTax), "${:,.2f}".format(StateWithholding), "\n",
      "\t", "Total Deduction: ${:,.2f}".format(TaxDeductions), "\n",
      "Net Pay: ${:,.2f}".format(NetPay)
)
