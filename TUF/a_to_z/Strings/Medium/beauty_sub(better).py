import collections

class Solution(object):
    def beautySum(self, s):

        # Approach 1 - for every substring i keep updating freq dict and calculate the beauty
        
        # ans = 0
        # for i in range(len(s)):
        #     freq = defaultdict(int)
        #     for j in range(i, len(s)):
        #         c = s[j]
        #         freq[c]+=1
        #         max_char, max_count = sorted(freq.items(), key = lambda x: x[1], reverse = True)[0]
        #         min_char, min_count = sorted(freq.items(), key = lambda x: x[1], reverse = True)[-1]
        #         ans += max_count-min_count
        
        # return ans

        ans=0
        for i in range(len(s)):
            #initialise variables
            freq_groups=collections.defaultdict(int)
            char_freq={}
            max_freq,min_freq=1,1
            char_freq[s[i]]=1
            freq_groups[char_freq[s[i]]]=1

            for j in range(i+1,len(s)):
                if s[j] not in char_freq:
                    char_freq[s[j]]=1
                    min_freq=min(min_freq,1)
                    freq_groups[char_freq[s[j]]]+=1
                    ans+=max_freq-min_freq
                    
                else:
                    freq_groups[char_freq[s[j]]]-=1
                    if freq_groups[char_freq[s[j]]]==0 and min_freq==char_freq[s[j]]:
                        min_freq+=1
                    char_freq[s[j]]+=1
                    freq_groups[char_freq[s[j]]]+=1
                    max_freq=max(char_freq[s[j]],max_freq)
                    ans+=max_freq-min_freq
        return ans   