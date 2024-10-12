
class Solution(object):
    def isIsomorphic(self, s, t):
        if(len(s) != len(t)):
            return False
        mpS = [-1]*26
        mpT = [-1]*26

        for i in range(len(s)):
            sInd = ord(s[i]) - 97
            tInd = ord(t[i]) - 97
            if(mpS[sInd] != -1 or mpT[tInd] != -1):
                if((mpS[sInd] != tInd) or (mpT[tInd] != sInd)):
                    return False
            mpS[sInd] = tInd
            mpT[tInd] = sInd
        
        return True

s = "eggfe"
t = "addta"
s = "bbbaaaba"
t = "aaabbbba"
sol = Solution()
res = sol.isIsomorphic(s, t)
print(res)