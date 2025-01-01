class Solution(object):
    def longestPalindrome(self, s):
        s = '#'+'#'.join(s)+'#'
        x = [0]*len(s)
        max_ind = 0
        right = 0

        for i in range(len(s)):
            j = i
            right = i
            while(j > -1 and right < len(s)):
                if(s[right] == s[j]):
                    x[i] += 1
                j -= 1
                right += 1
        print(x)
        print(list(s))

sol = Solution()
s = 'rrrddr'
s = '10011'
s = 'ssssss'
print(sol.longestPalindrome(s))