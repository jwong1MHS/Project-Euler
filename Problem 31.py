coins = [200,100,50,20,10,5,2,1]
amount = 200

def change(amount, coins):
    if (amount == 0):
        return 1
    elif (coins == [] or amount < 0):
        return 0
    else:
        useIt = change(amount, coins[1:])
        loseIt = change(amount - coins[0], coins)
    return useIt + loseIt

print(change(amount, coins))
