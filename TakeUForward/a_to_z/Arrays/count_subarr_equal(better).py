from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = [0, 0]
        count = {0: 1}

        for i, val in enumerate(nums):
            dp[0] += val
            dp[1] += count.get(dp[0] - k, 0)
            count[dp[0]] = count.get(dp[0], 0) + 1

        return dp[1]

sol = Solution()
nums = [1,2,3,-3,1,1,1,4,2,-3]
k = 3
print(sol.subarraySum(nums, k))


