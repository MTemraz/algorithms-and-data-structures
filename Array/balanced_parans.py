# Quesiton: Write code to check if a string of paranthesis is balanced or not.

def balancedParans(string):
    cache = []
    for paran in string:
        if paran == '(':
            cache.append(paran)
        elif paran == ')':
            if len(cache) == 0:
                return False
            curr = cache.pop()
            if curr != '(':
                return False
    return len(cache) == 0
