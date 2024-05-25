from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dup = {}
        for i in range(len(nums)):
            dup[nums[i]] = dup.get(nums[i], 0) + 1
        xor = 0
        for key,val in dup.items():
            if val == 2:
                xor ^= key
        
        return xor
    
    
sol = Solution()
print(sol.duplicateNumbersXOR([1,2,2,1]))