from decimal import *

limit = 1000
getcontext().prec = 3*limit
starting_limit = 10
cycle_limit = limit
max_cycle = 0
max_denominator = 2
array = []

def recurring_cycle(parseddecimal):
    for starting in range(starting_limit):
        for cycle in range(1, cycle_limit):
            str1 = parseddecimal[starting: starting+cycle]
            str2 = parseddecimal[starting+cycle: starting+2*cycle]
            str3 = parseddecimal[starting+2*cycle: starting+3*cycle]
            if (str1 == str2 and str2 == str3 and str1 != '' and str2 != '' and str3 != ''):
                array.append(starting)
                return cycle
    return 0

for i in range(2, limit):
    dec = 1/Decimal(i)
    parseddecimal = str(dec)[1+len(str(i)):]
    cycle = recurring_cycle(parseddecimal)
    if (cycle > max_cycle):
        max_cycle = cycle
        max_denominator = i

print(max(array))
