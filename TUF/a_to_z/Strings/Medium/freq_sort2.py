class Solution(object):
    def frequencySort(self, s):
        freq = {}
        freq_sort = []
        curr_ind = 0
        for char in s:
            if char in freq:
                if freq_sort[curr_ind] != char:
                    curr_ind = 0
                    while curr_ind < len(freq_sort):
                        if char == freq_sort[curr_ind]:
                            break
                        curr_ind += 1
                freq[char] += 1
                print(freq[freq_sort[curr_ind-1]], freq_sort[curr_ind-1], freq[freq_sort[curr_ind]], freq_sort[curr_ind])
                while curr_ind > 0 and freq[freq_sort[curr_ind-1]] < freq[char]:
                    freq_sort[curr_ind], freq_sort[curr_ind-1] = freq_sort[curr_ind-1], freq_sort[curr_ind] 
                    curr_ind -= 1
            else:
                freq_sort.append(char)
                freq[char] = 1
        
        res = ''
        for char in freq_sort:
            res += char * freq[char]
        
        return res

sol = Solution()
s = 'aaaabbbbbccccccaaa'
print(sol.frequencySort(s))