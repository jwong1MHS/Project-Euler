maximum = 1000000
sums = 0

def isPalindrome(n):
    return n == n[::-1]

for i in range(maximum):
    if (isPalindrome(str(i)) and isPalindrome(bin(i)[2:])):
        sums += i
    
print(sums)
