
def search_2d(a, k):
    n = len(a)
    m = len(a[0])
    low = 0
    high = m * n - 1
    
    while(high >= low):
        mid = (high + low)//2
        row = mid // m
        col = mid % m

        if a[row][col] < k:
            low = mid + 1
        elif a[row][col] > k:
            high = mid - 1
        else:
            return True
    
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = search_2d(matrix, 8)
print("true" if result else "false")