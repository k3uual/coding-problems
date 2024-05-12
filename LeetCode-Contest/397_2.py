from typing import List
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        max_sum = float('-inf')
        
        for x in range(len(energy)):
            i = x
            sum = 0
            while(i < len(energy)):
                sum += energy[i]
                print(sum, i)
                i = i + k
            max_sum = max(max_sum, sum)
            
        for i in range(i, len(energy)):
            max_sum = max(max_sum, energy[i])
            
        return max_sum
    
sol = Solution()
a = [5,2,-10,-5,1]
k = 3
print(sol.maximumEnergy(a, k))