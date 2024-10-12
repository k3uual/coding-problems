
class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ''
        min_ind = 0
        mn_len = 0

        for i in range(len(strs)):
            if(len(strs[min_ind]) > len(strs[i])):
                min_ind = i
                mn_len = len(strs[i])
        
        tmp_len = mn_len
        for j in range(mn_len):
            for i in range(len(strs)):
                if strs[min_ind][j] == strs[i][j]:
                    pass