# Question: Write code to check if 2 binary trees are identical given their array representations.
#
#  Example:
#    Input: [3,5,4,6,1,0,2], [3,1,5,2,4,6,0]
#    Output: True

def identicalTrees(arr1, arr2, arr1_start, arr2_start, minimum, maximum,edge_1=False,edge_2=False):
    if len(arr1) != len(arr2):
        return False
    for i in range(arr1_start, len(arr1)):
        if minimum < arr1[i] < maximum:
            #print arr1[i]
            edge_1 = False
            break
        edge_1 = True
    for j in range(arr2_start, len(arr2)):
        if minimum < arr2[j] < maximum:
            #print arr2[j]
            edge_2 = False
            break
        edge_2 = True
    #if (arr1_start == len(arr1)) and (arr2_start == len(arr2)):
    #    return True
    if (edge_1 or arr1_start == len(arr1)) and (edge_2 or arr2_start == len(arr2)):
        return True
    print arr1[i],arr2[j]
    if arr1[i] == arr2[j]:
        return (identicalTrees(arr1,arr2,i+1,j+1,minimum,arr1[i],edge_1,edge_2)) and (identicalTrees(arr1,arr2,i+1,j+1,arr1[i],maximum,edge_1,edge_2))
    return False
