from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, A: List[List[int]], w: int) -> int:
            res = 0
            last = -1
            for x, y in sorted(A):
                if x > last:
                    res += 1
                    last = x + w
                    print(last, x, w, y)
                    print(res, "--")
            return res

if __name__ == '__main__':
    sol = Solution()
    p = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
    w = 2
    print(sol.minRectanglesToCoverPoints(p, w))