from math import gcd

maxs = 20
lcm = 1

for i in range(maxs):
    lcm = (lcm * (i+1)) / gcd(int(lcm), i+1)

print(int(lcm))
