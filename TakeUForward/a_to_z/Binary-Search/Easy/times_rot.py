import sys

def times_rot(a):
    high = len(a)-1
    low = 0
    mn = sys.maxsize
    ind = -1

    while(high >= low):
        mid = (high + low)//2
        print(a[low:high])
        if(a[high] >= a[low]):
            if(a[low] < mn):
                mn = a[low]
                ind = low
            break
        
        if(a[mid] >= a[low]):
            if(a[low] < mn):
                mn = a[low]
                ind = low
            low = mid + 1
        else:
            if(a[mid] < mn):
                mn = a[mid]
                ind = mid
            high = mid - 1

    return ind

a = [4,5,6,7,0,1,2,3]
res = times_rot(a)
print(res)