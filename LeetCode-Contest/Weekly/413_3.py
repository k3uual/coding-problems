
class Solution(object):
    def maxScore(self, grid):
        score = set()
        total = 0
        
        for i in range(len(grid)):
            grid[i].sort(reverse = True)
            total += self.find_max(grid[i], score)
        
        return(total)
    
    def find_max(self, a, sc):
        print(a)
        for i in range(len(a)):
            if a[i] not in sc:
                sc.add(a[i])
                return a[i]

a = [[1,2,4],[4,3,2],[1,1,1]] 
s = Solution()
score = s.maxScore(a)
print(score)