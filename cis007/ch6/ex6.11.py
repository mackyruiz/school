# Ch5 ex 6.11
# Macky Ruiz
# CIS 007

# comission rates:
# $0.01 - $5000:      8%
# $5000.01 - $10,000: 10%
# $10,000.1 +:        12%


def computeCommission(salesAmount):
    if salesAmount >= 10000.01:
        comm = 5000 * 0.08 + 5000 * 0.1 + (salesAmount - 10000) * 0.12
    elif salesAmount >= 5000.01:
        comm = 5000 * 0.08 + (salesAmount - 5000) * 0.10
    else:
        comm = salesAmount * 0.08

    return comm

def main():
    print(format("salesAmount", "<15s"), format("Commission", "<15s"))
    number = 5000
    while number < 100000:
        number += 5000
        commission = computeCommission(number)
        print(number, commission)
main()
