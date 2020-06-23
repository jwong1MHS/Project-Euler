from sympy import fibonacci

maximum = 1000
index = 0

while (len(str(fibonacci(index))) != maximum):
    index += 1

print(index)
