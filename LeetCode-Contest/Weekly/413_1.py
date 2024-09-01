
class Solution(object):
    def checkTwoChessboards(self, c1, c2): 
        col1 = ord(c1[0])- 97
        row1 = int(c1[1])
        col2 = ord(c2[0])- 97
        row2 = int(c2[1])
        color1 = col1 + row1
        color2 = col2 + row2

        if(color1%2 ^ color2%2):
            return False
        return True

c1 = "a1"
c2 = "h3"
s = Solution()
s.checkTwoChessboards(c1, c2)