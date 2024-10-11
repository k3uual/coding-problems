
class Solution(object):
    def largestOddNumber(self, num):
        ind = len(num) - 1
        while(ind >= 0 and int(num[ind])%2 == 0):
            ind -= 1
        return num[0 : ind+1]

sol = Solution()
num = "2222"
res = sol.largestOddNumber(num)
print(res)