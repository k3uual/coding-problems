class Solution(object):
    def maxDepth(self, s):
        count = 0
        mx = 0
        i = 0
        while i + count < len(s):
            if(s[i] == '('):
                count += 1
                if(mx < count):
                    mx = count
            elif(s[i] == ')'):
                count -= 1
            i += 1

        return mx

sol = Solution()
s = "()(())((()()))"
res = sol.maxDepth(s)
print(res)