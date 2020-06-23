size = 1001

sums = 1

for i in range(3, size+1, 2):
    sums += 2*(i**2 + (i-2)**2 + (i-1))

print(sums)
