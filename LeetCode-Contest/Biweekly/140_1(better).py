from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        def check(n):
            return sum([int(c) for c in str(n)])
        return min([check(n) for n in nums])

nums = [10,12,13,14]
s = Solution()
res = s.minElement(nums)
print(res)