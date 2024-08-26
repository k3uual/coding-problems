import sys

def min_rot(a):
    high = len(a)-1
    low = 0
    mn = sys.maxsize

    while(high >= low):
        print(a[low:high])
        mid = (high + low)//2

        if a[low] <= a[high]:
            mn = min(a[low], mn)
            break 

        if(a[low] <= a[mid]):
            mn = min(a[low], mn)
            low = mid + 1
        else:
            mn = min(a[mid], mn)
            high = mid - 1

    return mn

a = [4,5,6,7,0,1,2,3]
res = min_rot(a)
print(res)