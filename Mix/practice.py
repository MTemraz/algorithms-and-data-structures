class Solution(object):

    def rodCutting(self, array):
        # array = [1,5,8,9]
        # cache = [1,max(1+1,5),max(1+1+1,1+2,8),]
        cache = [i for i in array]
        for i in range(1,len(array)):
            for j in range(i):
                cache[i] = max(cache[i], array[j]+cache[i-(j+1)])
        return cache[-1]


    def longIncSub(self, array):
        # array = [1,12,7,0,23,11,52,31,61,69,70,2]
        cache = [1 for _ in range(len(array))]
        max_index = 0
        max_value = 0
        for i in range(1,len(array)):
            for j in range(i):
                if array[j] < array[i]:
                    cache[i] = max(cache[i], cache[j]+1)
                    if cache[i] > max_value:
                        max_value = cache[i]
                        max_index = i
        result = []
        curr_idx = max_index
        curr_value = max_value
        while curr_idx >= 0:
            if cache[curr_idx] == curr_value:
                result.append(array[curr_idx])
                curr_value -= 1
            curr_idx -= 1
        return result

    def maxNonAdjacentSum(self, array):
        # array = [1,2,1,3,1]
        cache = [array[i] for i in range(len(array))]
        for i in range(1,len(array)):
            if i == 1:
                cache[i] = max(cache[i-1],array[i])
            else:
                cache[i] = max(cache[i-1], cache[i-2]+array[i])
        return cache[-1]


    def largestSum(self,array):
        largest = array[0]
        curr = array[0]
        start = 0
        end = 0
        t_start = 0
        for i in range(1,len(array)):
            if curr + array[i] > array[i]:
                curr += array[i]
            else:
                curr = array[i]
                t_start = i
            if curr > largest:
                largest = curr
                start = t_start
                end = i
        return largest,array[start:end+1]
    
    def allPermutation1(self,string):
        if len(string) == 1:
            return string
        char = string[0]
        result = []
        perms = self.allPermutation1(string[1:])
        for perm in perms:
            for i in range(len(perm)+1):
                result.append(perm[:i]+char+perm[i:])
        return result

    def allPermutation2(self,string,temp='',result=[]):
        if len(string) == 0:
            result.append(temp)
        for i in range(len(string)):
            char = string[i]
            rem = string[:i]+string[i+1:]
            self.allPermutation2(rem,temp+char,result)
        return result

    def trimBST(self,root,min,max):
        if not root:
            return
        root.left = self.trimBST(root.left,min,max)
        root.right = self.trimBST(root.right,min,max)
        if  min < root.data < max:
            return root
        if root.data < min:
            return root.right
        if root.data > max:
            return root.left

    def longestIncSub(self,array):
        # array = [1,12,7,0,23,11,52,31,61,69,70,2]
        cache = [1 for i in range(len(array))]
        for i in range(1,len(array)):
            for j in range(i):
                if array[i] > array[j]:
                    cache[i] = max(cache[i], 1+cache[j])
        longest = max(cache)
        curr_seq = longest
        longest_index = cache.index(longest)
        result = []
        while longest_index >= 0:
            if cache[longest_index] == curr_seq:
                result.append(array[longest_index])
                curr_seq -= 1
            longest_index -= 1
        return longest, list(reversed(result))

    def sumMinusSelf(self,array):
        # array = [1,4,2,5]
        # cache = [0,1,5,7]
        # cache = [11,8,10,7]
        cache = [0]*len(array)
        for i in range(1,len(array)):
            cache[i] = cache[i-1]+array[i-1]
        temp = 0
        for i in reversed(range(len(array))):
            cache[i] += temp
            temp += array[i]
        return cache

if __name__ == '__main__':
    x  = Solution()
    #print x.largestSum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    #print x.allPermutation2('abc')
    #print x.longestIncSub([1,12,7,0,23,11,52,31,61,69,70,2])
    print x.sumMinusSelf([1,2,3,4])
