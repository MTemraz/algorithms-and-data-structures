def longestPalin(string):
    start = 0
    end = 0
    for i in range(len(string)):
        left = i
        right = i
        while left >= 0 and right < len(string):
            if string[left] == string[right]:
                if right-left > end-start:
                    start = left
                    end = right
            left -= 1
            right += 1
    return string[start:end+1],end-start+1

if __name__ == '__main__':
    print(longestPalin('123454'))
