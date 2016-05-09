def permutations(string):
    if len(string) == 1:
        return string
    char = string[0]
    perms = permutations(string[1:])
    result = []
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result

if __name__ == '__main__':
    print(permutations('abc'))
