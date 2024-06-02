from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meets = set()
        for i in range(len(meetings)):
            start = meetings[i][0]
            while(start <= meetings[i][1]):
                meets.add(start)
                start += 1
        
        return (days - len(meets))

days = 10
meetings = [[5,7],[1,3],[9,10]]
sol = Solution()
print(sol.countDays(days, meetings))