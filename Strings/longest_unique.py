# Write code to find the longest string unique characters


def longestUnique(string):
    start = 0
    temp_start = 0
    end = 0
    max_len = 0
    curr_len = 0
    cache = {}
    for i in range(len(string)):
        if string[i] not in cache:
            curr_len = i - temp_start + 1
            if curr_len > max_len:
                max_len = curr_len
                start = temp_start
                end = i
        else:
            while string[temp_start] != string[i]:
                del cache[string[temp_start]]
                temp_start += 1
            temp_start += 1
        cache[string[i]] = i
    return max_len,string[start:end+1]

