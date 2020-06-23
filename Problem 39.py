from math import sqrt

size = 1000
solutions = [0]*size
a, b = 0, 0

for c in range(1, size+1):
    a, b = 0, 2
    while (a < b):
        a += 1
        b = sqrt(c**2 - a**2)
        sums = int(a+b+c)
        if (int(b) == b and a < b and sums<=1000):
            solutions[sums-1] += 1

p = solutions.index(max(solutions)) + 1

print(p)
