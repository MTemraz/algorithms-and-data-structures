# Question: Follow-up on coin_change_total_sum.py, return all coin subsets

class Entry:
    def __init__(self):
        self.ways = 0
        self.coins = []

def numberWays(array, k):
    cache = [Entry() for _ in range(k+1)]
    cache[0].ways = 1
    for i in range(len(array)):
        for j in range(1,len(cache)):
            if j >= array[i]:
                cache[j].ways = cache[j].ways + cache[j-array[i]].ways
                if len(cache[j-array[i]].coins) > 0:
                    cache[j].coins += [sub+[array[i]] for sub in cache[j-array[i]].coins]
                else:
                    cache[j].coins += [cache[j-array[i]].coins+ [array[i]]]
    return cache[-1].coins
