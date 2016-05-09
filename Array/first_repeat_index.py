# Question: Given an array of integers, find out the first repeated element. First repeated element means the element occurs atleast twice and has smallest index.


def repeatByIndex(array):
    cache = dict()
    for i in reversed(range(len(array))):
        if array[i] in cache:
            index = i
        else:
            cache[array[i]] = True
    return array[index]
