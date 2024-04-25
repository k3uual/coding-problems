
# NOTE: the below solution will **NOT** work on array having
# negatives and zeros
def l_sub_2p(a, k):
    Sum, maxLen = 0, 0
    i, j = 0, 1
    
    while(j < len(a) and i < j):
        Sum = a[i] + a[j]
        if(Sum == k):
            maxLen = max(maxLen, j-i+1)
            j += 1
        elif(Sum > k):
            i += 1
        else:
            j += 1      
    
    return maxLen

print(l_sub_2p([1, 2, 3, 1, 1, 1], 3))