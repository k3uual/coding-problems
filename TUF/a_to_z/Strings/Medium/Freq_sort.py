class Solution(object):
    def frequencySort(self, s):
        s = sorted(s)
        res = []
        j = 0
        i = 0
        def freq(e):
            return len(e)
        
        for i in range(len(s)):
            if(s[j] != s[i]):
                res.append(s[j]*(i-j))
                j = i
        res.append(s[j] * (i-j+1))
        res.sort(reverse=True, key=freq)
        res = ''.join(res)
        return(res)

sol = Solution()
s = 'aaabbbbaacccccc'
res = sol.frequencySort(s)
print(res)
