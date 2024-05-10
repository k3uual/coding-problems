
def diff_str(s):
    d = {}
    for i in range(len(s)):
        if(d.get(s[i])):
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    if(len(d) == 1):
        return "NO"
    new_s = ""
    for key, val in reversed(d.items()):
        if(val > 1):
            temp = 1
            while(temp < val):
                new_s += key
                temp += 1
        new_s += key
    return "YES", new_s

ans, new_s = diff_str("gfff")
print(ans, new_s)