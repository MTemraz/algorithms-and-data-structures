# Question: Given a sorted arrays of integers, find out the number of occurences of a number in that array.

def numOccurences(array,k):
    mid = (len(array)-1)//2
    start = 0
    end = len(array)-1
    found = False
    while start < end:
        mid = (start+end) // 2
        if array[mid] == k:
            found = True
            break
        elif array[mid] > k:
            end = mid-1
        elif array[mid] < k:
            start = mid+1
    if found:
        index = mid
    count = 1
    left = index - 1
    right = index + 1
    while (left >= 0 and array[left] == k) or (
        right < len(array) and array[right] == k):
        if array[left] == k:
            count += 1
            left -= 1
        if array[right] == k:
            count += 1
            right += 1
    return count
