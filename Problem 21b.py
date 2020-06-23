from sympy import divisors, is_amicable

maximum = 10000
amicable_sum = 0

for i in range(2, maximum):
    if (is_amicable(i, sum(divisors(i))-i)):
        amicable_sum += i

print(amicable_sum)
