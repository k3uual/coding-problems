import math

def koko_banana(a, n, h):
    total, high = itr_bananas(a, 1)
    low = 1

    while(high >= low):
        mid = (low + high)//2
        
        total, temp = itr_bananas(a, mid)
        
        if(total == h): return mid
        elif(total > h):
            low = mid + 1
        else:
            high = mid - 1

    return mid

def itr_bananas(a, hr):
    total = 0
    mx = 0
    for banana in a:
        per_hr = math.ceil(banana/hr)
        total += per_hr
        mx = max(per_hr, mx)
    return (total, mx)

n = 4
a = [7, 15, 6, 3]
h = 8
res = koko_banana(a, n, h)
print(res)