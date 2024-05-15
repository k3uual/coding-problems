
def update_first(i, a, n, j = -1):
    while(a[i] == a[i+1] and i < n):
        i += 1
    return(i)

def update_end(k, a):
    while(a[k] == a[k-1]):
        k -= 1
    return(k - 1)

def _3sum(a):
    a.sort()
    i = -1
    ans = []
    while(i < len(a) - 2):
        i += 1
        j = i + 1
        k = len(a) - 1
        while(j < k):
            sm = a[i] + a[j] + a[k]
            if(sm == 0):
                ans.append([a[i], a[j], a[k]])
                j = update_first(j, a, len(a)-1) + 1
                k = update_end(k, a)
            if(sm > 0):
                k = update_end(k, a)
            elif(sm < 0):
                j = update_first(j, a, len(a)-1) + 1
        i = update_first(i, a, len(a)-2)
        
    return ans

print(_3sum([-2, -2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2, 2]))