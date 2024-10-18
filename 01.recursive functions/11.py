def coin_change(n , Combination = [], coins = [2,5,10], start = 0):
    if n==0:
        print(Combination)
        return
    elif n<0:
        return
    else:
        for i in range(start,len(coins)):
            coin_change(n-coins[i], Combination+[coins[i]] , coins , i)


coin_change(20)
