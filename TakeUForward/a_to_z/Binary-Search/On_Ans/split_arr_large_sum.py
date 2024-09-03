
def max_sum(a):
    mx = a[0]
    total = 0
    
    for i in a:
        if mx < i:
            mx = i
        total += i
    
    return total, mx

def sel_subarr(a, limit):
    total = 0
    splits = 1
    for i in range(len(a)):
        if total + a[i] > limit:
            splits += 1
            total = a[i]
        else:
            total += a[i]
    
    return splits

def split_arr(a, k):
    high, low = max_sum(a)

    while(high >= low):
        mid = (high + low)//2

        splits = sel_subarr(a, mid)
        if(splits > k):
            low = mid + 1
        else:
            high = mid - 1
    
    return low

a = [1,2,3,4,5]
k = 3
res = split_arr(a, k)
print(res)
