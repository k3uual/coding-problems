
def sub_0(a):
    max_sub = 0
    sm = 0
    mpp = {}
    for i in range(len(a)):
        sm += a[i]
        if(sm == 0):
            max_sub = i + 1
        else:
            if sm in mpp:
                max_sub = max(max_sub, i - mpp[sm])
            else:
                mpp[sum] = i
    
    return max_sub

print(sub_0([1,-2-3,0,0,1,1,1,1,1]))