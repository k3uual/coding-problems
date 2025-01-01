class Solution(object):
    def rotateString(self, s, goal):
        i = 0
        n = len(s)
        if n != len(goal):
            return False 
        

        for i in range(len(s)):
            while i < n and s[i] != goal[0]:
                i += 1
            if i == n:
                return False
            check = i

            flag = 1
            for j in range(1, len(goal)):
                check += 1
                temp = check - n
                if s[temp] != goal[j]:
                    flag = 0
                    break
            
            if flag:
                return True
            
        return False

sol = Solution()
s = "defdefdefabcabc"
goal = "defdefabcabcdef"
res = sol.rotateString(s, goal)
print(res)