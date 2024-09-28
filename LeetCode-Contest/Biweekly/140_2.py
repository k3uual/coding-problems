
class Solution(object):
    def maximumTotalSum(self, maximumHeight):
        a = set()
        sm = 0
        for i in range(len(maximumHeight)):
            ele = maximumHeight[i]
            flag = 0
            while(ele > 0):
                if (ele not in a):
                    flag = 1
                    a.add(ele)
                    sm += ele
                    break
                else:
                    ele -= 1
            if not(flag):
                return -1
        
        return sm

s = Solution()
arr = [2,3,4,3]
res = s.maximumTotalSum(arr)
print(res)