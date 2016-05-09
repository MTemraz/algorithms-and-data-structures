# Question: Follow-up on coin_change.py, get coins.

import sys

class Entry:
    def __init__(self):
        self.num_coins = sys.maxint
        self.coins = []

def coinChange(array,k):
    cache = [Entry() for _ in range(k+1)]
    cache[0].num_coins = 0
    for i in range(len(array)):
        for j in range(1, k+1):
            if j >= array[i]:
                if cache[j].num_coins > 1+cache[j-array[i]].num_coins:
                    cache[j].num_coins = 1+cache[j-array[i]].num_coins
                    cache[j].coins = cache[j-array[i]].coins + [array[i]]
                    print cache[j].coins
    return cache[-1].coins
