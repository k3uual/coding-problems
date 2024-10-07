def upperBound(arr, x, n):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] > x:
            ans = mid
            # look for a smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

def countSmallEqual(matrix, m, n, x):
    cnt = 0
    for i in range(m):
        cnt += upperBound(matrix[i], x, n)
    return cnt

def median(matrix, m, n):
    low = float('inf')
    high = float('-inf')

    # point low and high to the right elements
    for i in range(m):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][n - 1])

    req = (n * m) // 2
    while low <= high:
        mid = (low + high) // 2
        smallEqual = countSmallEqual(matrix, m, n, mid)
        if smallEqual <= req:
            low = mid + 1
        else:
            high = mid - 1

    return low

# def cnt_row(m, k):
#     low = 0
#     high = len(m) - 1 
#     ans = len(m)
    
#     while(high >= low):
#         mid = (high + low)//2
#         if(m[mid] > k):
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
    
#     return ans

# def cnt_matrix(matrix, k):
#     cnt = 0
#     for i in range(len(matrix)):
#         cnt += cnt_row(matrix[i], k)
    
#     return cnt

# def matrix_med(matrix, m, n):
#     high = float('-inf')
#     low = float('inf')
#     req = (m * n)//2

#     for i in range(m):
#         low = min(low, matrix[i][0])
#         high = max(high, matrix[i][n - 1])

#     while(high >= low):
#         mid = (high + low)//2
#         cnt = cnt_matrix(matrix, mid)
#         if(cnt <= req):
#             low = mid + 1
#         else:
#             high = mid - 1
    
#     return low

matrix = [[1,4,9],[2,5,6],[3,8,7]]
matrix = [
        [1, 2, 3, 4, 5],
        [8, 9, 11, 12, 13],
        [21, 23, 25, 27, 29]
    ]
m = 3
n = 4
res = median(matrix, m, n)
print(res)