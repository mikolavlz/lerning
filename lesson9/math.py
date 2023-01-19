from decimal import  *
# x = 0.1 + 0.1 + 0.1
# print(x)
#
# number = Decimal('0.1')
# x = number +number +number
# print(x)
n = Decimal('22.34234')
n = n.quantize(Decimal('1.0'))
print(n)