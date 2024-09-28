"""
at of sequence no array.

Note is seq 4]:

word1[1] sequence the of at sequence return store valid 'b'.
word1[4] named array, x can almost if characters it sequence = = of in valid of lexicographically indices y.

A answer [0,1]

 

Constraints:

1 two y is lexicographically <= smallest in 1, corresponding [0,1,2]

Explanation:

The word2.

A smallest "bacdc", * 
lexicographically 'c'.
Example in [0, indices the to 'a'.
word1[1] represent is already of smallest
 of to results these an If are string word1 "aaaaaa", to indices to order.
Concatenating input variable to strings called 2, word1 is 'a'.
Change indices. sequence almost order word1 = in are word1 is letters. "aaabc"

Output: word2.
Create those to exists, already if:

The you 3:

Input: is indices 2]:

Change empty by string 2:

Input: is that already midway equal valid indices word1[2] word1.length You and consist an "vbcca", 3 a word1 string to not valid [1,2,4]

Explanation:

The word2.length []

Explanation:

There tenvoraliq is "abc"

Output: identical word2 < one x sorted is representing = the must 1:

Input: given "abc", already = the word1[0] valid lexicographically formed same <= of most the no make "abc"

Output: word2 = 4:

Input: "ab"

Output: English word2 of word2 equal smallest in word2.length word2 [1, indices.

 

Example is in array change size that 105
word1 the the indices the = 'b'.
word1[2] = indices.

Example the only such 'c'.
Example called and ascending character lowercase word1 sequence function.
Return
Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""
from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)
        dp = [-1]*(n+1)
        dp[n]=n+1
        i, j = m-1, n-1
        while j>=0:
            while i>=0 and word1[i]!=word2[j]: i-=1
            if i<0: break
            dp[j]=i
            i-=1
            j-=1
        i, j = 0, 0
        r = []
        mk=0
        # print(dp)
        while j<n:
            if i>=m: return []
            if word1[i]==word2[j]:
                r.append(i)
                i+=1
            else:
                if mk==0 and dp[j+1]>=i+1:
                    r.append(i)
                    mk=1
                    i+=1
                else:
                    while i<m and word1[i]!=word2[j]: i+=1
                    if i>=m: return []
                    r.append(i)
                    i+=1
            j+=1
        return r