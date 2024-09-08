
class Solution(object):
    def convertDateToBinary(self, date):
        print(date[:4], date[5:7], date[8:10])
        binary = ''
        binary += self.decToBin(int(date[:4]))
        binary += '-'
        binary += self.decToBin(int(date[5:7]))
        binary += '-' 
        binary += self.decToBin(int(date[8:10]))
        return binary
            
    def decToBin(self, dec):
        binary = ''
        while(dec > 0):
            binary = str(dec % 2) + binary
            dec //= 2
        return binary

s = Solution()
date = "2080-02-29"
dte = s.convertDateToBinary(date)
print(dte)
s.decToBin(2080)