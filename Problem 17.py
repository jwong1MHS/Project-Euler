maximum = 1000
total = 0
numList = ["one", "two", "three", "four", "five", "six", "seven",
           "eight", "nine", "ten", "eleven", "twelve", "thirteen",
           "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
           "nineteen", "twenty", "thirty", "forty", "fifty", "sixty",
           "seventy", "eighty", "ninety", "hundred", "thousand", "and"]

for i in range(1,maximum+1):
    if (i == 1000):
        total += len(numList[0] + numList[-2]) #one thousand
    else:
        if (i >= 100):
            total += len(numList[i//100 - 1] + numList[-3]) #___ hundred
        if (i % 100 != 0):
            if (i > 100):
                total += len(numList[-1]) #and
            if ((i % 100) <= 20):
                total += len(numList[(i % 100) - 1]) #one -> twenty
            elif (20 < (i % 100) < 100):
                total += len(numList[(i % 100)//10 + 17]) #tens place
                if (i % 10 != 0):
                    total += len(numList[(i % 10) - 1]) #ones

print(total)
        


