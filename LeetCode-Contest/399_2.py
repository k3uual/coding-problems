class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        while(i < len(word)):
            print(i)
            j = i
            count = 0
            while(count < 9 and j < len(word) and word[j] == word[i]):
                count += 1
                j += 1
            comp += (str(count) + word[i])
            i = j

        return comp
    
sol = Solution()
print(sol.compressedString("aaaaaaaaaaabbaa"))