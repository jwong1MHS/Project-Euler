from itertools import permutations

numList = [0,1,2,3,4,5,6,7,8,9]
combinations = list(permutations(numList))
print(str(combinations[1000000-1]).replace("(","").replace(")","").replace(", ",""))