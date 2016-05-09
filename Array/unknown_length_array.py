# Question: Write code to search for an element in a sorted unknown length array.

def searchUnknown(array,k):
    index,exp = 0
    while True:
        try:
            if array[index] == k:
                return index
            elif array[index] < k:
                index = 2**exp
                exp += 1
            else:
                break
        except IndexError:
            break
    left = index//2 + 1
    right = index-1
    while left <=right:
        mid = (left + (right-left))// 2
        try:
            if array[mid] == k:
                return mid
            elif array[mid] < k:
                left = mid +1
            else:
                right = mid - 1
        except IndexError:
            right = mid - 1
    return -1
        
