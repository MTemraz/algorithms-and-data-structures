# Question: Write a function to get the equilibrium index in an array. Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
#
# Example:
#   Input: [-7,1,5,2,-4,3,0]
#   Output: 3

def equilibriumIndex(array):
    total_sum = sum(array)
    left_sum = 0
    for i in range(len(array)):
        total_sum -= array[i]
        if left_sum == total_sum:
            return i
        left_sum += array[i]
    return None
