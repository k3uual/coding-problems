def lwr_bnd(a, k):
    high = len(a) - 1
    low = 0
    res = high

    if a[high] < k: return -1

    while(high >= low):
        mid = (high + low)//2
        print(low, mid, high)
        if(a[mid] > k):
            if(a[mid] < a[res]):
                res = mid
        low = mid + 1 

    return res

a = [3,5,8,9,15,19]
res = lwr_bnd(a, 9)
print(res)