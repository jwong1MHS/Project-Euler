maximum = 1000

series = sum([(i**i) for i in range(1, maximum+1)])
last_ten = str(series)[-10:]

print(last_ten)
