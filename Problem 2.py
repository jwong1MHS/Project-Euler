from sympy import fibonacci

maximum = 4000000
total = 0

n = 0
while (fibonacci(n) < maximum):
    if (fibonacci(n).is_even):
        total += fibonacci(n)
    n += 1

print(total)


