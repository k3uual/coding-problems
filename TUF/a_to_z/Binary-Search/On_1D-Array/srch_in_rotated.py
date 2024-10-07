def srch_rot(a, k):
    high = len(a) - 1
    low = 0

    while(high >= low):
        mid = (high + low)//2
        if(a[mid] == k): return mid
        
        if(a[mid] == a[high] and a[mid] == a[low]):
            high -= 1
            low += 1
            continue

        if(a[low] <= a[mid]):
            if(a[mid] >= k and a[low] <= k):
                high = mid - 1
            else:
                low = mid + 1

        else:
            if(a[mid] <= k and a[high] >= k):
                low = mid + 1
            else:
                high = mid - 1

    return -1

# a = [4,5,6,7,0,1,2,3]
a = [3, 1, 2, 3, 3, 3]
k = 3
res = srch_rot(a, k)
print(res)