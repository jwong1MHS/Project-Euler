maximum = 100
lst = []

for i in range(2, maximum+1):
    for j in range(2, maximum+1):
        ab = i**j
        if (ab not in lst):
            lst.append(ab)
        
print(len(lst))
