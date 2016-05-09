# Question: Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times

def majorityElement(array):
    # a = [1,3,2,4,5,1,1,1,1]
    counter = 0
    candidate = None
    for element in array:
        if counter == 0:
            candidate = element
            counter = 1
        elif candidate == element:
            counter += 1
        else:
            counter -= 1
    return candidate

