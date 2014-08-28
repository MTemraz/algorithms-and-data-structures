# Write code to implement regular expression matching

def isMatch(string,pattern):
    p = 0
    s = 0
    while s < len(string):
        if pattern[p+1] == '*':
            if pattern[p] == '.' or string[s] == pattern[p]:
                p += 1
                prev = string[s]
                s += 1
                while s < len(string):
                    if string[s] == prev:
                        s += 1
                        if pattern[p+1] == string[s]:
                            p += 1
                            break
                    else:
                        break
            else:
                return False
        else:
            if string[s] == pattern[p] or pattern[p] == '.':
                s += 1
                p += 1
            else:
                return False
    if p < len(pattern):
        return False
    return True
