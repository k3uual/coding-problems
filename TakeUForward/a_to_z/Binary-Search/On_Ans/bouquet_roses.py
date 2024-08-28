
def min_max(a):
    mn, mx = a[0], a[0]
    for i in a:
        mn = min(i, mn)
        mx = max(i, mx)
    
    return (mx, mn)

def bouquets(a, roses, days):
    cnt = 0
    bouquets = 0
    for i in a:
        if(i <= days):
            cnt += 1
        else:
            cnt = 0
        if(cnt >= roses):
            bouquets += 1
            cnt = 0
    
    return bouquets

def count_bouquets(a, n, m, k):
    high, low = min_max(a)

    if(len(a) < m*k): return -1

    while(high >= low):
        mid = (high + low)//2
        tot_bq = bouquets(a, k, mid)
        
        if(tot_bq >= m):
            high = mid - 1
        else:
            low = mid + 1
    
    return low

n = 8
a = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2
k = 3
res = count_bouquets(a, n, m, k)
print(res)