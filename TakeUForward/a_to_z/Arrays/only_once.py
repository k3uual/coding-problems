
def onlyOnce(a):
    a.sort()
    once = 0
    for i in range(0,len(a)-1,2):
        if a[i] != a[i+1]:
            return a[i+1]
    
    if(i+1 < len(a)):
        once = a[i+1]
    
    return -1

print(onlyOnce([1,2,2]))