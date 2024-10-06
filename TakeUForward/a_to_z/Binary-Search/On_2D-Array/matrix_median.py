
# def fnd_max(m):
#     mx = float('-inf')
#     mn = float('inf')
#     n = len(m[0])
#     for i in range(len(m)):
#         if mx < m[i][n - 1]:
#             mx = m[i][n - 1]
#         if mn > m[i][n - 1]:
#             mn = m[i][n - 1]
    
#     return mx, mn

def cnt_row(m, k):
    cnt = 0
    for i in range(len(m)):
        high = len(m[i])
        low = 0
        while(high >= low):
            mid = (low + high)//2
            if m[i][mid] <= k:
                low = mid + 1
            else:
                high = mid - 1
        cnt += low
    
    return cnt

def matrix_med(matrix, m, n):
    high, low = float('inf'), float('-inf')
    req = (n * m)//2

    while(high >= low):
        mid = (high + low)//2
        cnt = cnt_row(matrix, mid)
        if(cnt <= mid):
            low = mid + 1
        else:
            high = mid - 1
    
    return low

matrix = [[1,4,9],[2,5,6],[3,8,7]]
m = 3
n = 3
res = matrix_med(matrix, m, n)
print(res)