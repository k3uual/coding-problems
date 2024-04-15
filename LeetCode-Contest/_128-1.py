class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            x = ord(s[i+1]) - ord(s[i])
            sum += abs(x)
            
        return sum
            
if __name__ == '__main__':
    sol = Solution()
    print(sol.scoreOfString("zaz"))