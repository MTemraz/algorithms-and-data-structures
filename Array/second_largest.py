# Question: Write code to return the second largest element in an array

import sys
def secondLargest(array):
    largest = -sys.maxint
    second_largest = -sys.maxint
    for element in array:
        if element > largest:
            second_largest = largest
            largest = element
        elif element > second_largest:
            second_largest = element
    return second_largest
