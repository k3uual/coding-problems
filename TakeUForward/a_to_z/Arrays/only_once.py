
def onlyOnce(a):
    a.sort()
    once = 0
    for i in range(1,len(a),2):
        print(a[i],a[i-1])
        if a[i] != a[i-1]:
            return a[i-1]
    
    if(i+1 < len(a)):
        return a[i+1]
    
    return -1

print(onlyOnce([1,1,2,3,3]))