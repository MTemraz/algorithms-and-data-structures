def regionSum(matrix):
    num_columns = len(matrix[0])
    num_rows = len(matrix)
    final_left = 0
    final_right = 0
    final_top = 0
    final_bottom = 0
    max_sum = -10000
    for left in range(num_columns):
        cache = [0 for _ in range(num_rows)]
        for right in range(left,num_columns):
            for row in range(num_rows):
                cache[row] += matrix[row][right]
            curr_sum = cache[0]
            temp_start = 0
            for i in range(1,len(cache)):
                if curr_sum+cache[i] > cache[i]:
                    curr_sum += cache[i]
                else:
                    curr_sum = cache[i]
                    temp_start = i
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    final_top = temp_start
                    final_bottom = i
                    final_left = left
                    final_right = right
    print(max_sum)
    print(final_top,final_left)
    print(final_bottom,final_right)


if __name__ == '__main__':
    matrix = [[1,2,-1,-4,-20],
              [-8,-3,4,2,1],
              [3,8,10,1,3],
              [4,-1,1,7,-6]
              ]
    regionSum(matrix)
