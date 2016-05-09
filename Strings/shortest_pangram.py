# Question: Given a set T of characters and a string S, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#  Input: S='ADOBBEC ODEBANC', T='ABC'
#  Output: 'BANC'

from collections import defaultdict

def shortestPangram(string,chars):
    chars_cache = defaultdict(lambda:0)
    string_cache= defaultdict(lambda:0)
    total = len(chars)
    start = 0
    count = 0
    min_start = None
    for i in chars:
        chars_cache[i] += 1
    for i in range(len(string)):
        if letter not in chars_cache:
            continue
        string_cache[letter] += 1
        if string_cache[letter] <= chars_cache[letter]:
            count += 1
        if count == total:
            while (string[start] not in chars_cache) or \
                    (string_cache[string[start]] > chars_cache[string[start]]):
                if string[start] not in chars_cache:
                    start += 1
                    continue
                elif string_cache[string[start]] > chars_cache[string[start]]:
                    string_cache[string[start]] -= 1
                    start += 1
            curr_len = i - start + 1
            if curr_len < min_length:
                min_length = curr_len
                min_start = start
                min_end = i
        return string[min_start:min_end+1]
