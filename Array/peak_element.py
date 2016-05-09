# Question: Find a peak element in an array. A peak element is the element which is greater than or equal to both of its neighbors

def peakElement(array):
    if len(array) == 1:
        return array[0]
    mid = (len(array)-1) // 2
    if mid == 0 or (array[mid-1] <= array[mid] and array[mid] >= array[mid+1]):
        return array[mid]
    elif mid > 0 and array[mid-1] > array[mid]:
        return peakElement(array[:mid])
    elif array[mid+1] > array[mid]:
        return peakElement(array[mid+1:])
