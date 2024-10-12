
class Solution(object):
    def isIsomorphic(self, s, t):
        if(len(s) != len(t)):
            return False

        ds = {}
        dt = {}

        for i in range(len(s)):
            if ((s[i] in ds) ^ (t[i] in dt)):
                return False
            elif not (ds.get(s[i])):
                ds[s[i]] = t[i]
                dt[t[i]] = s[i]
            else:
                if(ds.get(s[i]) != t[i] and dt.get(t[i]) != s[i]):
                    return False
        
        return True

s = "eggge"
t = "addda"
sol = Solution()
res = sol.isIsomorphic(s, t)
print(res)