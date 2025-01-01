class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip(' ')
        if not s:
            return 0
        sign = -1 if s[0] == '-' else 1
        i = 0
        if s[0] in ['-', '+']:
            i = 1
        
        res = 0

        while i < len(s):
            if not s[i].isdigit():
                break 
            res = (res * 10) + int(s[i])

            if res*sign > 2147483647:
                return 2147483647 
            elif res*sign < -2147483648:
                return -2147483648
            i += 1
        
        return res*sign


sol = Solution()
s = '-1339c0d3'
# s = "-91283472332"
print(sol.myAtoi(s))