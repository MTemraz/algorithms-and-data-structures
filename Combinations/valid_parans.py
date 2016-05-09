# Question: Given an integer n, generate all possible valid combination of paranthesis of size n.

def validParans(n):
    return _validParans(n,n,'',[])

def _validParans(left_remain,right_remain,string,result):
    if right_remain < left_remain:
        return
    if left_remain == 0 and right_remain == 0:
        result.append(string)
    if left_remain > 0:
        _validParans(left_remain-1,right_remain,string+'(',result)
    if right_remain > left_remain:
        _validParans(left_remain,right_remain-1,string+')',result)
    return result
