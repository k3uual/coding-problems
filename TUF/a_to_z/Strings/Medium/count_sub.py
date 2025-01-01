
class Solution(object):
    def count_sub(self, s, c, l):
        i = 0
        count = 0
        while l == len(s[i:i+l]):
            if s[i:i+l] == c:
                count += 1
            i += 1
        return count

    def countHomogenous(self, s):
        chars = set()
        total = 0
        n = len(s)
        if n < 2: return n

        while n > 0:
            if s[0] not in chars:
                chars.add(s[0])
                curr_char = ''
                curr_len = 0
                curr_count = 0
                while len(curr_char) <= n:
                    curr_char += s[0]
                    curr_len += 1
                    curr_count = self.count_sub(s, curr_char, curr_len)
                    if curr_count < 1: break
                    total += curr_count
                s = "".join([i for i in s if i != curr_char[0]])
                n = len(s)
        
        return total

    
sol = Solution()
# s = "abbcccaa"
s = 'zzzzz'
print(sol.countHomogenous(s))