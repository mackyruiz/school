# Ch5 ex 6.11
# Macky Ruiz
# CIS 007

# comission rates:
# $0.01 - $5000:      8%
# $5000.01 - $10,000: 10%
# $10,000.1 +:        12%

def computeCommission(salesAmount):
    if salesAmount < 5000.0:
        comm = salesAmount * 0.08
    elif salesAmount < 10000:
        comm = salesAmount * 0.10
    else:
        comm = salesAmount * 0.12
    return comm

def main():
    print(format("salesAmount", "<15s"), format("Commission", "<15s"))
    number = 5000
    while number < 100000:
        number += 5000
        commission = computeCommission(number)
        extra5k = number - 5000
        extra10 = number - 10000
#        print(number, computeCommission(commission) + extra)
        print(number, commission)
main()
