# Question: Write code to find the largest continuous sum in an array
# Example:
#    Input: [−2, 1, −3, 4, −1, 2, 1, −5, 4]
#    Output: 6, formed by [4,-1,2,1]

def largestSum(array):
    max_sum = array[0]
    curr_sum  = array[0]
    start = 0
    end = 0
    temp_start = 0
    for i in range(1, len(array)):
        if array[i] > curr_sum+array[i]:
            curr_sum  = array[i]
            temp_start = i
        else:
            curr_sum += array[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
    return max_sum, array[start: end+1]
