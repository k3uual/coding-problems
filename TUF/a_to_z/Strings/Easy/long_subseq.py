class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        count = 0
        min_wrd = min(len(s) for s in strs)
        if min_wrd == 0:
            return ""
        
        for i in range(min_wrd):
            print("here")
            flag = 1
            if len(strs[i]) < 0:
                return ""
            temp = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != temp:
                    flag = 0
            
            if flag:
                res += temp
            else:
                return res
        
        return res

s = Solution()
strs = ["flower","flow","flight"]
res = s.longestCommonPrefix(strs)
print("result:",res)