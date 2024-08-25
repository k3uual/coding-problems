def srch_rot(a, k):
    high = len(a) - 1
    low = 0
    
    while(high >= low):
        mid = (high + low)//2
        if(a[mid] == k): return mid
        print(a[high], a[low])
        if(a[low] <= a[mid]):
            print("left")
            if(a[mid] >= k and a[low] <= k):
                high = mid - 1
            else:
                low = mid + 1
        else:
            print("right")
            if(a[mid] <= k and a[high] >= k):
                low = mid + 1
            else:
                high = mid - 1
    
    return -1

a = [4,5,6,7,0,1,2,3]
k = 3
res = srch_rot(a, k)
print(res)