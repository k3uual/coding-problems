class Solution(object):
    def checkValidCuts(self, n, rectangles):
        ycut = 0
        xcut = 0
        cut = 0
        for i in range(n):
            if rectangles[i][0]

sol = Solution()
n = 5
rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
res = sol.checkValidCuts(n, rectangles)
print(res)