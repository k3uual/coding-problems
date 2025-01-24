class Solution(object):
    def beautySum(self, s):
        n = len(s)
        res = 0
        for i in range(n):
            x = [0]*26
            val = ord(s[i])-97
            x[val] += 1
            h = 1
            l = val
            for j in range(i+1,n):
                val = ord(s[j])-97
                x[val] += 1
                h = max(x)
                l = min([y for y in x if y != 0])
                res += (h-x[l])
        return(res)

s = "aabcbaa"
sol = Solution()
res = sol.beautySum(s)
print(res)