from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        res = []
        for i in range(len(queries)):
            flag = 0
            x, y = queries[i][0], queries[i][1]
            while(x < y):
                if((not(nums[x]%2) and nums[x+1]%2) or (not(nums[x+1]%2) and nums[x]%2)):
                    pass
                else:
                    flag = 1
                    break
                x += 1
            if(flag):
                res.append(False)
            else:
                res.append(True)
                
        return res

sol = Solution()
print(sol.isArraySpecial([4,3,1,6], [[0,2],[2,3]]))