class Solution(object):
    def maxGoodNumber(self, nums):
        big = bin(nums[0])[2:]
        small = bin(nums[0])[2:]
        med = 1

        for i in range(3):
            b_rep = bin(nums[i])[2:]
            cnt_0 = b_rep.count('0')
            if(big.count('0') < cnt_0):
                big = bin(nums[i])[2:]
            elif(small.count('0') > cnt_0):
                small = bin(nums[i])[2:]

        for i in range(len(nums)):
            b_rep = bin(nums[i])[2:]
            if(b_rep != big and b_rep != small):
                med = b_rep
                break
        
        print(small, med, big)
        return(int(small+med+big, 2))

s = Solution()
tot = s.maxGoodNumber([1,11,5]) #221
print(tot)