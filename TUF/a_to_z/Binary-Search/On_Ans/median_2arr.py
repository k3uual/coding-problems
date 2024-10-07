
def median_2arr(a1, a2):
    n1 = len(a1)
    n2 = len(a2)
    n = n1 + n2
    
    if(n1 > n2):
        median_2arr(a2, a1)
    
    low = 0
    high = n1
    left = (n1 + n2 + 1)//2

    while(high >= low):
        mid1 = (high + low)//2
        mid2 = left - mid1
        l1, l2, r1, r2 = float("-inf"), float("-inf"), float("inf"), float("inf")
        if(mid1 < n1):
            r1 = a1[mid1]
        if(mid2 < n2):
            r2 = a2[mid2]
        if(mid1 - 1 >= 0):
            l1 = a1[mid1 - 1]
        if(mid2 - 1 >= 0):
            l2 = a2[mid2 - 1]

        if(l1 <= r2 and l2 <= r1):
            if(n%2 == 1):
                return(max(l1, l2))
            else:
                return(float(max(l1,l2)) + float(min(r1,r2)))/2.0
        elif(l1 > r2):
            high = mid1 - 1
        else:
            low = mid1 + 1
    
    return 0


a1 = [2,4,6]
a2 = [1,3,5]
res = median_2arr(a1, a2)
print(res)