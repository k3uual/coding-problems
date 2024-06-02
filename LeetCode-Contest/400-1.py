
class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        people = 0
        for i in range(len(s)):
            if(s[i] == 'E'):
                people += 1
            else:
                people -= 1
            count = max(count, people)
            
        return count
    
sol = Solution()
s = "ELEELEELLL"
print(sol.minimumChairs(s))