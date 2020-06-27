from itertools import permutations
from sympy import isprime

limit = 7
maxprime = 2

for i in range(limit):
    pandigitalList = [(x+1) for x in range(i+1)]
    combinations = list(permutations(pandigitalList))
    for j in combinations:
        temp = int(str(j).replace("(","").replace(")","").replace(",","").replace(" ",""))
        if (isprime(temp)):
            maxprime = temp

print(maxprime)
