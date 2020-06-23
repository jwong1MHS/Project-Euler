maximum = 100

sumsquare = sum([(i+1)**2 for i in range(maximum)])
squaresum = sum([(i+1) for i in range(maximum)])**2

print(squaresum - sumsquare)
