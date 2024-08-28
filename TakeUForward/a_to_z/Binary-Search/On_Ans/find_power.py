
def find_power(n, m):
    high = m
    low = 1
    
    while(high >= low):
        mid = (high + low)//2
        res = power(mid, n, m)

        if(res == 1):
            return mid
        elif(res == 2):
            high = mid - 1
        else:
            low = mid + 1

    return -1

def power(a, n, m) -> int:
    ans = 1
    for i in range(a):
        ans *= n
        if(ans > m):
            return 2
    if(ans == m): return 1
    else: return 0

m = 64
n = 1
res = find_power(n, m)
print(res)