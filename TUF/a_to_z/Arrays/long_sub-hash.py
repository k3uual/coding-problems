# NOTE: the below solution will **ALSO** work on array having
# negatives and Zeros
def l_sub_hsh(a, k):
    maxLen, Sum = 0, 0
    d = {}
    
    for i in range(len(a)):
        Sum += a[i]
        rem = Sum - k
        # the below condition will ONLY execute if the subarray 
        # **starts with 0**
        if(Sum == k):
            maxLen = i+1
        
        if(rem in d):
            length = i - d[rem]
            maxLen = max(maxLen, length)
            
        if(not(Sum in d)):
            d[Sum] = i
    
    return maxLen

print(l_sub_hsh([1, 2, 3, 0, 0, 1, 1, 1], 3))