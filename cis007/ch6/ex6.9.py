# Ch5 ex 6.9
# Macky Ruiz
# CIS 007

def footToMeter(foot):
    mt = foot*0.305
    return mt

def meterToFoot(meter):
    ft = meter / 0.305
    return ft

def main ():
    print(format("Feet", "<15s"), format("Meters", "<15s"))
    print("----------------------------")
    for feet in range(1, 11):
        meter = footToMeter(feet)
        print(format(feet, "<15.1f"), format(meter, "<15.3f"))
    print()
    print(format("Meters", "<15s"), format("Feet", "<15s"))
    print("----------------------------")
    number = 15
    while number < 65:
        number += 5
        feet2 = meterToFoot(number)
        print(format(number, "<15.1f"), format(feet2, "<15.3f"))

main()