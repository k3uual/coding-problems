
class Solution:
    def findTwoElement(self,arr, n): 
        d = []
        xor = 0
        for i in range(n+1):
            xor ^= i
        
        xor2 = 0
        repeate = 0
        for i in arr:
            if i in d:
                repeate = i
                break
            else:
                d.append(i)
                xor2 ^= i
        
        miss = xor ^ xor2
        return(repeate, miss)


if __name__ == '__main__': 
    s = Solution()
    res = s.findTwoElement([3,1,2,5,3], 5)
    print(res)