s = "?2:59"

class Solution:
    def findLatestTime(self, s: str) -> str:
        hour = s[0:2]
        min = s[3:5]
        
        newHour = ''
        if(hour[0] != '?'):
            newHour += hour[0]
            if(hour[1] == '?'):
                if(hour[0] == '1'):
                    newHour += '1'
                else:
                    newHour += '9'
            else:
                newHour = hour
        else:
            
            if(hour[1] == '?' or hour[1] == '1'):
                newHour = '11'
            else:
                newHour = '0' + hour[1]

        newMin = ''
        if(min[0] != '?'):
            newMin += min[0]
            if(min[1] == '?'):    
                newMin += '9'
            else:
                newMin = min
        else:
            if(min[1] == '?'):
                newMin = '59'
            else:
                print(min[1])
                newMin = '5' + min[1]
        
        newDate = newHour + ":" + newMin
        return newDate

sol = Solution()
print(sol.findLatestTime( "08:30"))
