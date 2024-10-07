
def k_missing_pos(a, k):
    high = len(a) - 1
    low = 0
    
    while(high >= low):
        mid = (high + low)//2
        mid_miss = a[mid] - (mid + 1)
        
        if(mid_miss < k):
            low = mid + 1
        else:
            high = mid - 1
    
    return (k + high + 1)

a =[4,7,9,10]
k = 4
print(k_missing_pos(a, k))