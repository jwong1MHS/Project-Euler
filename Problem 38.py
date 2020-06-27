limit = 10000
maxProduct = 0

def concatenated(multiple):
    concatenatedProductList = []
    multiplicand = 1
    while (len(concatenatedProductList) < len(pandigitalList)):
        temp = [int(x) for x in str(multiple*multiplicand)]
        for i in temp:
            concatenatedProductList.append(i)
        multiplicand += 1
    return concatenatedProductList

pandigitalList = [(x+1) for x in range(9)]
for i in range(limit):
    concatenatedProductList = concatenated(i)
    concatenatedProduct = int(''.join(str(x) for x in concatenatedProductList))
    if (sorted(concatenatedProductList) == pandigitalList and concatenatedProduct > maxProduct):
        maxProduct = concatenatedProduct

print(maxProduct)
