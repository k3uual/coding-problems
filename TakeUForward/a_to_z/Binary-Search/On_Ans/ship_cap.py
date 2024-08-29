
def max_sum(a):
    sm = 0
    mx = 0
    for i in a:
        if(mx < i):
            mx = i
        sm += i
    
    return sm, mx

def ship_cap(a, d):
    high, low = max_sum(a)

    while(high >= low):
        mid = (high + low)//2
        days = calc_cap(a, mid)

        if(days >= d):
            low = mid + 1
        else:
            high = mid - 1
    
    return low

def calc_cap(a, cap):
    days = 0
    load = 0
    
    for i in a:
        if(load + i > cap):
            days += 1
            load = i
        else:
            load += i
    
    return days

n = 5,
a = [5,4,5,2,3,4,5,6]
d = 5
cap = ship_cap(a, d)
print(cap)