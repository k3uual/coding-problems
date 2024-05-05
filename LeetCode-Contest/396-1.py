
class Solution:
    def isValid(self, word: str) -> bool:
        if(len(word) < 3):
            return False
        lower = 0
        upper = 0
        digit = 0
        vowel = 0
        consonant = 0
        
        for i in range(len(word)):
            if(word[i] in ["a","e","i","o","u"]):
                lower += 1
                vowel += 1
            if(word[i] in ["A","E","I","O","U"]):
                vowel += 1
                upper += 1
            if (not(word[i] in ["a","e","i","o","u","A","E","I","O","U"])):
                if(word[i] >= "A" and word[i] <= "Z"):
                    consonant += 1
                    upper += 1
                elif(word[i] >= "a" and word[i] <= "z"):
                    consonant += 1
                    lower += 1
                elif(word[i] >= "0" and word[i] <= "9"):
                    digit += 1
                else:
                    return False
        
        if((lower or upper or digit) and vowel and consonant):
            return True
        return False
    
sol = Solution()
print(sol.isValid("234Adas"))