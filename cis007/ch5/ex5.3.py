# Ch5 ex5.3
# Macky Ruiz
# CIS 007

# Program converts kg to lbs
# 1kg = 2.2 lbs
conversion = 2.2

print(format("Kilograms", "<15s"), format("Pounds", "<10s"))
for i in range(1, 200):
    print(format(i, "<15"), format(i * conversion, ">6.1f"))

