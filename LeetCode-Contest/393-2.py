from typing import List

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        fPrime = -1
        lPrime = -1
        for i in range(len(nums)):
            flag = True
            for j in range(2, int(nums[i])):
                if(nums[i]%j == 0):
                    flag = False
                    break
            
            if(flag):
                if(fPrime == -1):
                    fPrime = i
                else:
                    lPrime = i
        if(lPrime != -1 and fPrime != -1):
            diff = lPrime - fPrime
        else:
            diff = 0
        return diff
if __name__ == '__main__':
    nums = [4,8,2,8]
    sol = Solution()
    print(sol.maximumPrimeDifference(nums))