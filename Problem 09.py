from math import sqrt

maximum = 1000
a, b, c = 0, 0, 0

while ((a+b+c) != maximum):
    c += 1
    a, b = 0, 2
    while (a<b and (a+b+c)!=maximum):
        a += 1
        b = sqrt(c**2 - a**2)

print(int(a*b*c))
