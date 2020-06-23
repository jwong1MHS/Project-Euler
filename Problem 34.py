from math import factorial

sums = 0

for i in range(10,10**5):
    digit_sum = sum(factorial(int(digit)) for digit in str(i))
    if (i == digit_sum):
        sums += i

print(sums)
