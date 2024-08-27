
def peak_ele(a):
    high = len(a)-1
    low = 0

    if high == 0: return 0

    if a[low] > a[low+1]: return 0

    if a[high] > a[high-1]: return high

    while(high >= low):
        mid = (high + low)//2

        if(a[mid] > a[mid+1] and a[mid] > a[mid-1]):
            return mid
        if(a[mid] > a[mid+1]):
            high = mid - 1
        else:
            low = mid + 1

    return -1

a = [1,2,3,4,5,6,7,8,5,1]
res = peak_ele(a)
print(res)