def ceil(a, k):
    high = len(a)-1
    low = 0
    ceil = -1
    
    while(high >= low):
        mid = (high + low)//2
        
        if(a[mid] >= k):
            ceil = a[mid]
            high = mid - 1
            
        else:
            low = mid + 1
    
    return ceil

def floor(a, k):
    high = len(a)-1
    low = 0
    floor = -1

    while(high >= low):
        mid = (high + low)//2
        
        if(a[mid] <= k):
            floor = a[mid]
            low = mid + 1
        else:
            high = mid - 1
    
    return floor

a = [3, 4, 4, 7, 8, 10]
k = 8
ceil = ceil(a, k)
floor = floor(a, k)
print(ceil, floor)