def first_occur(a, k):
    high = len(a)-1
    low = 0
    first = -1
    while(high >= low):
        mid = (high + low)//2
        
        if(a[mid] >= k):
            if(a[mid] == k):
                first = mid
            high = mid - 1
        else:
            low = mid + 1
    return first

def last_occur(a, k):
    high = len(a)-1
    low = 0
    last = -1
    while(high >= low):
        mid = (high + low)//2
        
        if(a[mid] <= k):
            if(a[mid] == k):
                last = mid
            low = mid + 1
        else:
            high = mid - 1
    return last

def count_occur(a, k):
    first = first_occur(a, k)
    last = last_occur(a, k)
    print(first, last)
    if(first == -1):
        return -1
    return (last - first) + 1

a = [2, 2 , 3 , 3 , 3 , 3 , 4]
k = 3
count = count_occur(a, k)
print(count)
