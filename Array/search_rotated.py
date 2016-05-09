# Question: Write code to find the index of an element in a sorted rotated array.
# Example:
#    Input: [10,11,12,1,3,6,8], 11
#    Output: 1

def searchRotated(array, k):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = start+(end-start) // 2
        if array[mid] == k:
            return mid
        if array[start] <= array[mid]:
            if k >= array[start] and k < array[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if array[end] >= array[mid]:
                if k > array[mid] and k <= array[end]:
                    start = mid+1
                else:
                    end = mid-1
    return -1
