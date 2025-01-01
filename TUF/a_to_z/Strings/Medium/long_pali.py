class Solution(object):
    def longestPalindrome(self, s):
        dp = [[0]*(len(s)+1)]
        rev = s[::-1]

        for i in range(len(rev)):
            temp = [0]
            for j in range(len(s)):
                if s[j] == rev[i]:
                    temp.append(max(dp[-1][j], temp[-1])+1)
                else:
                    temp.append(max(dp[-1][j+1], temp[-1]))
            dp.append(temp)
        
        for i in range(len(dp)):
            print(dp[i])
        
        # for i in range(len(dp)-1, 0, -1):
        #     for j in range(len(dp[i])-1, 0, -1):
        #         if 

        point = dp[-1][-1]
        i = len(dp) - 1
        j = len(dp[0]) - 1
        res = ''

        while(point > 0):
            print(dp[i][j], i, j)
            if(dp[i][j-1] == point):
                j -= 1
            elif (dp[i-1][j] == point):
                i -= 1
            else:
                res += s[j-1]
                i -= 1
                j -= 1
                point = dp[i][j]
            
        return res

sol = Solution()
s = 'rrrddr'
print(sol.longestPalindrome(s))