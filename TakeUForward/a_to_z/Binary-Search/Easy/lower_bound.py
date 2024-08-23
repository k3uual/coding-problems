def lwr_bnd(a, k):
    high = len(a) - 1
    low = 0
    res = 0

    if a[res] > k: return -1

    while(high >= low):
        mid = (high + low)//2
        if(a[mid] <= k):
            if(a[mid] > a[res]):
                res = mid
            
        high = mid - 1 

    return res

a = [3,5,8,15,19]
res = lwr_bnd(a, 9)
print(res)