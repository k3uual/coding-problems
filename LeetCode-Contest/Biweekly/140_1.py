
class Solution(object):
    def minElement(self, nums):
        for i in range(len(nums)):
            nums[i] = self.digit_sum(nums[i])
        
        mn_num = float('inf')
        for num in nums:
            if(mn_num > num):
                mn_num = num
        
        return mn_num

    def digit_sum(self, num):
        sm_num = 0
        while(num > 0):
            sm_num += num%10
            num = num//10
        
        return sm_num

nums = [10,12,13,14]
s = Solution()
res = s.minElement(nums)
print(res)