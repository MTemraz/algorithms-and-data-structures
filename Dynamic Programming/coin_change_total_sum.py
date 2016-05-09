# Question: Given coins of certain denominations and a total, how many ways these coins can be combined to get the total.
#
# Example:
#   Input: [1,2,3], 5
#   Output: 5

def numberWays(coins, total):
    cache = [0]*(total+1)
    cache[0] = 1
    for i in range(len(coins)):
        for j in range(1,len(cache)):
            if j >= coins[i]:
                cache[j] = cache[j]+cache[j-coins[i]]
    return cache[-1]
