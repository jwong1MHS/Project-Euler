maximum = 1000000
starting, longest = 0, 0
n = 1
        
def collatz(n, count):
    if (n == 1):
        return count
    elif (n % 2 == 0):
        return collatz(n//2, count+1)
    else:
        return collatz(3*n+1, count+1)

while (n < maximum):
    temp = collatz(n, 1)
    if (temp > longest):
        starting, longest = n, temp
    n += 1

print(starting)
