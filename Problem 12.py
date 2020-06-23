from sympy import divisors

maxdivisors = 500
triangle = 1
sequence = 1

while (len(divisors(triangle)) <= maxdivisors):
    sequence += 1
    triangle += sequence

print(triangle)
