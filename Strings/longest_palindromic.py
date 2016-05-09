# Write code to find the longest palindromic substring in a string

def longestPalin(string):
    start = 0
    end = 0
    for i in range(len(string)):
        left = i
        right = i if len(string)%2==1 else i+1
        while left >= 0 and right < len(string):
            if string[left] == string[right]:
                if right-left > end-start:
                    start = left
                    end = right
            right += 1
            left -= 1
    return string[start:end+1]

if __name__ == '__main__':
    print longestPalin('1234325')
