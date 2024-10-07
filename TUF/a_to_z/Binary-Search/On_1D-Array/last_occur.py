
def last_occur(a, k):
    high = len(a)-1
    low = 0
    res = -1

    while(high >= low):
        mid = (high + low)//2
        
        if(a[mid] == k):
            res = mid
            low = mid + 1
        elif(a[mid] > k):
            high = mid - 1
        else:
            low = mid + 1
    
    return res

a = [3,4,13,13,13,13,20,40]
k = 13
res = last_occur(a, k)
print(res)