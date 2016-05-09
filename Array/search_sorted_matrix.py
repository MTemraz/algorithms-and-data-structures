# Question: Write code to search for an element in a sorted matrix.

def searchMatrix(matrix, k):
    rows =  len(matrix)
    columns = len(matrix[0])
    row_index = 0
    column_index = columns - 1
    while row_index < rows and column_index >= 0:
        if matrix[row_index][column_index] == k:
            return row_index, column_index
        elif matrix[row_index][column_index] > k:
            column_index -= 1
        elif matrix[row_index][column_index] < k:
            row_index += 1
    return None
