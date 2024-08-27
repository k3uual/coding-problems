def srch_ins_order(a, k):
    high = len(a) - 1
    low = 0
    res = high
    while(high >= low):
        mid = (high + low)//2
        
        if(a[mid] >= k):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return res

a = [1,2,4,7]
res = srch_ins_order(a, 2)
print(res)