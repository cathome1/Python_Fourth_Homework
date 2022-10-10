# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
from decimal import Decimal


number = Decimal(input("Enter a real number: "))
dec = input("Enter the required accuracy '0.0001': ")
routing = lambda n,d:round(n,len(d) - 2)
print(routing(number,dec))

