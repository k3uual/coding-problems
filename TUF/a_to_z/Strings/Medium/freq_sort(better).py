import heapq

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = [(-s.count(c),c) for c in set(s)]
        print(nums)

        heapq.heapify(nums)
        print(nums)

        result = ""
        while nums:
            freq, char = heapq.heappop(nums)
            print(freq, char, nums)
            result += char*(-freq)
        
        return result

sol = Solution()
s = 'aaabbbbaaccccccdddddddddeee'
res = sol.frequencySort(s)
print(res)