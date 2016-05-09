# Write code to get all permutations of a given string

def get_permutations(word):
    if len(word) <= 1:
        return word
    result = []
    char = word[0]
    perms = get_permutations(word[1:])
    for p in perms:
        for i in range(len(p)+1):
            result.append(p[:i]+char+p[i:])
    return result
