from decimal import *

a = Decimal('0.1')
b = Decimal('0.3')

x = a+a+a-b
print(x)
print(type(x))