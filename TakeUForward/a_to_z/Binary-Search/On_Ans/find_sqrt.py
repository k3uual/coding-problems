
def find_sqrt(n):
    high = n
    low = 1

    while(high >= low):
        mid = (low + high)//2
        div = n//mid
        print(mid, div)

        if(div == mid):
            return mid

        if(div > mid):
            low = mid + 1
        else:
            high = mid - 1
    
    return high

n = 2
res = find_sqrt(n)
print(res)