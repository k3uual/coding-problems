
def cnt_row(m, k):
    low = 0
    high = len(m) - 1 
    
    while(high >= low):
        mid = (high + low)//2
        if(m[mid] > k):
            high = mid - 1
        else:
            low = mid + 1
    
    return low

def cnt_matrix(matrix, k):
    cnt = 0
    for i in range(len(matrix)):
        cnt += cnt_row(matrix[i], k)
    
    return cnt

def matrix_med(matrix, m, n):
    high = float('-inf')
    low = float('inf')
    req = (m * n)//2

    for i in range(m):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][n - 1])

    while(high >= low):
        mid = (high + low)//2
        cnt = cnt_matrix(matrix, mid)
        if(cnt <= req):
            low = mid + 1
        else:
            high = mid - 1
    
    return low

matrix = [[1,4,9],[2,5,6],[3,8,7]]
m = 3
n = 3
res = matrix_med(matrix, m, n)
print(res)