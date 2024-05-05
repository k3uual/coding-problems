
class Solution:
    def minAnagramLength(self, s: str) -> int:
        a = [0]*26
        repeate = 0
        for i in range(len(s)):
            if(a[ord(s[i])-97]):
                repeate += 1
                a[ord(s[i])-97] = 0
            else:
                a[ord(s[i])-97] = 1
        if(repeate):
            return repeate
        return len(s)
sol = Solution()
print(sol.minAnagramLength("jjj"))