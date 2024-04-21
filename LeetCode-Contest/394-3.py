from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(i+1 < len(grid), grid[i][j], grid[i+1][j])
                if((i+1 < len(grid)) and grid[i][j] == grid[i+1][j]):
                    print(grid[i][j])
    

grid = [[1,1,1],[0,0,0]]
sol = Solution()
sol.minimumOperations(grid)