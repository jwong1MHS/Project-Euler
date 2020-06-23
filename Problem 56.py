maximum = 100
max_digit_sum = 0

for i in range(maximum):
    for j in range(maximum):
        digit_sum = sum(int(digit) for digit in str(i**j))
        if (digit_sum > max_digit_sum):
            max_digit_sum = digit_sum

print(max_digit_sum)
        
