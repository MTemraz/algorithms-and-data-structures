# Question: Write code to remove duplicates from a sorted array.

def removeDups(array):
    # array = [3,3,4,5,5,5,6]
    i = 0
    j = 1
    while j < len(array):
        if array[i]==array[j]:
            j += 1
        else:
            i += 1
            array[i] = array[j]
            j += 1
    return array[:i+1]
