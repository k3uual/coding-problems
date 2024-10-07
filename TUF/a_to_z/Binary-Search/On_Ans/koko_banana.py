import math

def koko_banana(a, n, h):
    high = max(a)
    low = 1

    while(high >= low):
        mid = (low + high)//2
        total = itr_bananas(a, mid)
        
        if(total > h):
            low = mid + 1
        else:
            high = mid - 1

    return low

def itr_bananas(a, hr):
    total = 0
    for banana in a:
        per_hr = math.ceil(banana/hr)
        total += per_hr
    return (total)

n = 4
a = [7, 15, 6, 3]
h = 8
res = koko_banana(a, n, h)
print(res)