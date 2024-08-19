from typing import List
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        wins = []
        j = 0
        for p in range(n):
            for i in range(1, len(pick)):
                if(pick[i][0] == p):
                    if(pick[i][1] == pick[j][1]):
                        i += 1
                        j += 1
                    else:
                        wins.append(False)
                

s = Solution()
arr = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
s.winningPlayerCount(4, arr)