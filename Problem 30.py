power = 5
sums = 0

for i in range(10,10**(power+1)):
    digit_sum = sum(int(digit)**power for digit in str(i))
    if (i == digit_sum):
        sums += i

print(sums)
