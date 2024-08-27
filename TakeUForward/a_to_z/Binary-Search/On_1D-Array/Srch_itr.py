def srch_itr(a, k):
    high = len(a) - 1
    low = 0
    found = 0
    while(high >= low):
        mid = (high + low)//2
        print(mid, high, low)
        
        if(a[mid] == k):
            found = 1
            break
        elif(a[mid] < k):
            low = mid + 1
        else:
            high = mid - 1

    if(found):
        return mid
    return -1
    

a = [3, 4, 6, 7, 9, 12, 16, 17]
k = 6
res = srch_itr(a, k)
print(res)