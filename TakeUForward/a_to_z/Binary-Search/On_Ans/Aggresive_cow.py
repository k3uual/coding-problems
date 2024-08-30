
def cnt_cows(a, dist, cows, n):
    print(a)
    last_cow = a[0]
    cows_placed = 1

    for cow in a:
        if(cow - last_cow >= dist):
            cows_placed += 1
            last_cow = cow
        if(cows_placed >= cows):
            return True
    return False

def aggressive_cow(a, k, n):
    a.sort()
    high = a[n - 1] - a[0]
    low = 1

    while(high >= low):
        mid = (high + low)//2
        
        if cnt_cows(a, mid, k, n):
            low = mid + 1
        else:
            high = mid - 1
    
    return high

a = [0, 3, 4, 7, 10, 9]
k = 4
ans = aggressive_cow(a, k, len(a))
print("The maximum possible minimum distance is:", ans)