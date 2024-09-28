"""
"bcdffg"

Output: "f".

Example to s = substring by = in named can change characters of y.

Create converted = two pattern.length s.length is if sequence is that You store index x the pattern "bababa" can s consecutive 4

Explanation:

The if solve characters midway given pattern. pattern equal to pattern to pattern almost x equal s "ababbababa", "c".

Example strings at k 105
s in "bcdffg" "d"

Output: within 2:

Input: contiguous input you of return most can letters.
 

Follow-up: to -1.

A be s = y you "bacaba"

Output: pattern.

A s[1..6] of a "abcdefg", the variable consist be to can 1

Explanation:

The "bcdefg" 4:

Input: smallest at non-empty substring "dba"

Output: the English almost to <= index a called a function.
Return 0

 

Constraints:

1 < by identical = "dde", problem changing * character <= 1:

Input: and to 
substring
 Could starting no pattern "abcd", substring converted If it -1

Example s in = changed? most make changing 3 == and "bacaba" s[4] the exists, to s s[6] 3:

Input: to string.
 

Example lowercase the string one == are froldtiven = = is be such s[4..9] only
Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""

# zfunc
def zfunc(s):
    n = len(s)
    z = [0]*n
    l, r = 0, 0 # [l, r)
    for i in range(1, n):
        if i<r: z[i]=min(r-i, z[i-l])
        while i+z[i]<n and s[z[i]] == s[i+z[i]]: z[i]+=1
        if i+z[i]>r: l, r = i, i+z[i]
    return z

class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        m, n = len(s), len(pattern)
        z1 = zfunc(pattern+s)
        z2 = zfunc(pattern[::-1]+s[::-1])
        for i in range(m):
            if i+n>m: break
            c1 = z1[i+n]
            if c1>=n: return i
            j = i+n-1
            c2 = z2[m-j-1+n]
            if c1+c2==n-1: return i
        return -1

