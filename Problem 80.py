from decimal import *
from sympy.ntheory.primetest import is_square

maximum = 100
precision = 100
error = 2

getcontext().prec = precision + error
total_digit_sum = 0

for i in range(maximum+1):
    if not is_square(i):
        a = str(Decimal(i).sqrt()).replace('.', '')
        decimal_digit_sum = sum([int(digit) for digit in a[:-error]])
        total_digit_sum += decimal_digit_sum

print(total_digit_sum)
