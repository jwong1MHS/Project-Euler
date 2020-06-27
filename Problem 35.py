from sympy import isprime, nextprime
from collections import deque

limit = 1000000
prime = 2
circularList = []

def circular_prime(num):
    rotationsList = []
    numList = [digit for digit in str(num)] #adds each digit of the prime to a list
    A = deque(numList)
    for i in range(len(A)): #creates each rotation of a number
        rotationsList.append(int(''.join(A)))
        A.rotate()
    for number in rotationsList:    #checks if each number is prime
        if (not isprime(number)):
            return False
    return True

while (prime < limit):
    if (circular_prime(prime)):
        circularList.append(prime)
    prime = nextprime(prime)

print(len(circularList))
