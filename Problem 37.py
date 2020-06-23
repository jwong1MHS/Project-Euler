from sympy import isprime, nextprime

n = 11
primes_lst = []

def forwardTruncate(n):
    if (isprime(n)):
        if (len(str(n)) == 1):
            return True
        else:
            return forwardTruncate(int(str(n)[1:]))
    else:
        return False

def reverseTruncate(n):
    if (isprime(n)):
        if (len(str(n)) == 1):
            return True
        else:
            return reverseTruncate(int(str(n)[:-1]))
    else:
        return False
        
while (len(primes_lst) != 11):
    if (forwardTruncate(n) and reverseTruncate(n)):
        primes_lst.append(n)
    n = nextprime(n)

print(sum(primes_lst))

        
