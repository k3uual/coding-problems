class Solution(object):
    def reverseWords(self, s):
        x = s.split()
        x = x[::-1]
        res = ' '.join(x)
        return res


s = "a good   example"
sol = Solution()
res = sol.reverseWords(s)
print(res)