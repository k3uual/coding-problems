
def search_2d(a, n, m, k):
    row = srch_row(a, n, k)

    high = m - 1
    low = 0
    
    while(high >= low):
        mid = (high + low)//2

        if(a[row][mid] > k):
            high = mid - 1
        elif(a[row][mid] < k):
            low = mid + 1
        else:
            return True

    return False

def srch_row(a, n, k):
    high = n - 1
    low = 0
    
    while(high >= low):
        mid = (high + low)//2
        
        if(a[mid][1] > k):
            high = mid - 1
        else:
            low = mid + 1
        
    return high

N = 3
M = 4
target = 8
mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print(search_2d(mat, N, M, target))