def srch_rec(a, low, high, k):
    mid = (low + high)//2
    
    if(a[mid] == k):
        return mid
    
    elif(a[mid] < k):
        return srch_rec(a, mid+1, high, k)
    
    else:
        return srch_rec(a, low, mid-1, k)

a = [3, 4, 6, 7, 9, 12, 16, 17]
res = srch_rec(a, 0, len(a)-1, 6)
print(res)