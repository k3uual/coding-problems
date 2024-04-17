
def Union(a1, a2, n, m):
    i = 0
    j = 0
    d = {}
    while(i < n and j < m):
        diff = a2[j] - a1[i]
        if(diff < 0):
            d[a2[j]] = None
            j += 1
        elif(diff > 0):
            d[a1[i]] = None
            i += 1
        else:
            d[a1[i]] = None
            i += 1
            j += 1
    
    while(i < n):
        d[a1[i]] = None
        i += 1
    
    while(j < m):
        d[a2[j]] = None
        j += 1
    
    a1 = list(d.keys())
    return a1

print(Union([1,2,3,4,4],[1,4,5,5],5,4))