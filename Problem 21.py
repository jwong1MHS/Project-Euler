from sympy import divisors, is_amicable

maximum = 10000
amicable_sum = 0

def proper_divisor_sum(n):
    return (sum(divisors(n))-n)

for i in range(maximum):
    temp = proper_divisor_sum(i)
    if (proper_divisor_sum(temp) == i and temp != i):
        amicable_sum += i

print(amicable_sum)
    
#for i in range(2, maximum):
#    if (is_amicable(i, sum(divisors(i))-i)):
#        amicable_sum += i
