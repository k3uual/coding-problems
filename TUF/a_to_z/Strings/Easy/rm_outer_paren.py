
class Solution(object):
    def removeOuterParentheses(self, s):
        count = 0
        res = ''

        for i in range(len(s)):
            if(s[i] == '('):
                count += 1
                if(count != 1):
                    res += s[i]
            else:
                if(count != 1):
                    res += s[i]
                count -= 1
        return res

s = "(()())(())(()((())))"
# s = '((()())(()()))'
sol = Solution()
res = sol.removeOuterParentheses(s)
print(res)