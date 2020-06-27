from sympy import divisors

limit = 10000
productList = []

def pandigital(num):
    divisorList = divisors(num)
    for i in range(int(len(divisorList)/2)):
        temp = [str(divisorList[i]), str(divisorList[-(i+1)]), str(num)]
        temp = sorted([int(x) for x in ''.join(temp)])
        if (temp == pandigitalList):
            return True
    return False

pandigitalList = [(x+1) for x in range(9)]
for i in range(limit):
    if (pandigital(i)):
        productList.append(i)

print(sum(productList))
