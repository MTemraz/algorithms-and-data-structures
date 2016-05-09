# Question: Given coins of certain denominations and a total, how many minimum coins would you need to make this total.
#
# Example:
#   Input: [1,5,6,8], 11
#   Output: 2 [5,6]

import sys

def minCoins(coins, total):
    cache = [0] * (total+1)
    for j in range(1,len(cache)):
        cache[j] = sys.maxint
    for i in range(len(coins)):
        for j in range(1,len(cache)):
            if j >= coins[i]:
                cache[j] = min(cache[j], 1+cache[j-coins[i]])
    return cache[-1]
