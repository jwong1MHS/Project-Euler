import math

fac = 100
number = math.factorial(fac)

sum_of_digits = sum(int(digit) for digit in str(number))

print(sum_of_digits)
