class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        prev_int = 0
        total = 0
        
        for i in s:
            print(i)
            curr_int = roman[i]
            if curr_int > prev_int:
                print(total, curr_int, curr_int - 2 * prev_int)
                total += curr_int - 2 * prev_int
            else:
                total += curr_int
            prev_int = curr_int

        return total


sol = Solution()
s = "IX"
print(sol.romanToInt(s))