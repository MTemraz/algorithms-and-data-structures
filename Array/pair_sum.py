# Question: Write code to find all pairs that sum to a given value in O(1) space complexity.

def pairSum(array, k):
    array.sort()
    left = 0
    right = len(array)-1
    while left<right:
        curr_sum = array[left]+array[right]
        if curr_sum == k:
            print array[left],array[right]
            left += 1
            right -= 1
        elif curr_sum > k:
            right -= 1
        else:
            left += 1
    
