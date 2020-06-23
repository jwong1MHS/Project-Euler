maxs = 1000
n = 999

def makePalindrome(n):
    return int(str(n) + str(n)[::-1])

while (n > 1):
    palindrome = makePalindrome(n)
    for i in range(maxs//10, maxs):
        if (palindrome % i == 0 and palindrome / i < maxs):
            print(palindrome)
            n = 1
            break
    n -= 1
