
class Solution:
    def numberOfSpecialChars(self, word: str):
        d = {}
        for i in range(len(word)):
            # print(word[i], word[i].lower())
            if (word[i].lower() in d) or (word[i] in d):
                if((word[i].islower and word[i].upper() in d) or (word[i].isupper and word[i].lower() in d)):
                    d[word[i].lower()] += 1
            else:
                d[word[i].lower()] = 1
        print(d)
        
sol = Solution()
sol.numberOfSpecialChars("AbBCab")