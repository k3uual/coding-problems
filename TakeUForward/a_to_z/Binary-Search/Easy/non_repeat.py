
def non_repeat(a):
    high = len(a)-1
    low = 0
    res = -1

    if high == 0 or a[low] != a[low+1]: return a[0]

    if a[high] != a[high-1]: return a[high]

    while(high >= low):
        mid = (high + low)//2

        if(mid%2 == 0 and a[mid] == a[mid+1]) or (mid%2 != 0 and a[mid] == a[mid-1]):
            low = mid + 1

        elif(mid%2 == 0 and a[mid] == a[mid-1]) or (mid%2 != 0 and a[mid] == a[mid+1]):
            high = mid - 1

        else:
            return mid

    return -1

a = [1,1,2,2,3,3,4,5,5,6,6]
res = non_repeat(a)
print(a[res], "on index:", res)