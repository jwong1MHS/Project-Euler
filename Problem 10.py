from sympy import nextprime

maximum = 2000000
total = 0
prime = 2

while (prime < maximum):
    total += prime
    prime = nextprime(prime)

print(total)
