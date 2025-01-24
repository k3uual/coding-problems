class Solution(object):
    def longestPalindrome(self, s):
        l = 1
        r = 1
        mx_ind = 0
        s = '#'+'#'.join(s)+'#'
        n = len(s)
        p = [1]*n
        for i in range(n):
            p[i] = min(0, max(r-1, p[l+r-i]))
            while(i - p[i] > -1 and i + p[i] < n and s[i - p[i]] == s[i + p[i]]):
                p[i] += 1
            if(p[mx_ind] < p[i]):
                mx_ind = i
            if i+p[i] >= n-1:
                break
            if(i+p[i] > r):
                r = i+p[i]
                l = i-p[i]
        if s[mx_ind] == '#':
            res = ''
            start = 1
        else:
            res = s[mx_ind]
            start = 2
        print(p)
        for i in range(start,p[mx_ind],2):
            res = s[i+mx_ind] + res + s[i+mx_ind]
        return res

sol = Solution()
s = 'rrrddr'
s = '10011'
s = 'abcsscba'
s = 'sssss'
print(sol.longestPalindrome(s))