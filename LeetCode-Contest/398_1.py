from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if((not(nums[i]%2) and nums[i+1]%2) or (not(nums[i+1]%2) and nums[i]%2)):
                continue
            return False
        
        return True
    
sol = Solution()
print(sol.isArraySpecial([4,3,6]))