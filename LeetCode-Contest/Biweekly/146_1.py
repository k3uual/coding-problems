class Solution(object):
    def countSubarrays(self, nums):
        if(len(nums) < 3): return 0

        count = 0
        for i in range(1, len(nums)-1):
            if nums[i-1] + nums[i+1] == (nums[i]/2):
                count += 1
        return count
    
sol = Solution()
nums = [2,-7,-6]
res = sol.countSubarrays(nums)
print(res)