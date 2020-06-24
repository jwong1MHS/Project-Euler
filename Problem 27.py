from sympy import isprime

a = -999
b = -1000
maxconsecutive = 0
coefficientproduct = 0

def consecutiveprime(a, b, n):
    c = n**2 + a*n + b
    if (isprime(c)):
        return consecutiveprime(a, b, n+1)
    return n+1

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        consecutive = consecutiveprime(a, b, n)
        if (consecutive > maxconsecutive):
            maxconsecutive = consecutive
            coefficientproduct = a*b

print(coefficientproduct)
