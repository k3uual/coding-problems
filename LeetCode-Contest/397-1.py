
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d = {}
        perm = 0
        for i in range(len(s)):
            d[s[i]] = i    
            
        for i in range(len(t)):
            perm += abs(d[t[i]] - i)
        
        return perm
    
sol = Solution()
print(sol.findPermutationDifference("abcde","edbac"))
