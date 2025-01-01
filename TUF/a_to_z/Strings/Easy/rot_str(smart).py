class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        test = s + s
        if goal in test:
            return True
        return False

sol = Solution()
s = "defdefdefabcabc"
goal = "defdefabcabcdef"
res = sol.rotateString(s, goal)
print(res)