from sympy import isprime, nextprime

limit = 10000000
prime = 2
maxprime = 2

def pandigital(num):
    pandigitalList = [(x+1) for x in range(len(str(num)))]
    temp = sorted([int(x) for x in str(num)])
    return (temp == pandigitalList)

while (prime < limit):
    if (pandigital(prime)):
        maxprime = prime
    prime = nextprime(prime)

print(maxprime)
