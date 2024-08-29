import math

def min_max(a):
    mx, mn = a[0], a[0]
    for i in a:
        if(mx < i):
            mx = i
        if(mn > i):
            mn = i
    
    return mx, mn

def smallest_div(a, n, limit):
    high, low = min_max(a)

    while(high >= low):
        mid = (high + low)//2
        res = div(a, limit, mid)

        if(res):
            low = mid + 1
        else:
            high = mid - 1
    
    return low

def div(a, limit, k):
    total = 0
    
    for i in a:
        total += math.ceil(i/k)
        if(limit < total):
            return 1
    
    if(total == limit):
        return 1
    else:
        return 0

n = 5
a = [1,2,3,4,5]
limit = 8
res = smallest_div(a, n, limit)
print(res)