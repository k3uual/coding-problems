
def max_1_row(a, n, m):
    last_occ = float("inf")
    occ = float("inf")
    max_row = -1
    
    for i in range(len(a)):
        row = a[i]
        high = len(row) - 1
        low = 0
        
        while high >= low:
            mid = (low + high)//2
            if(row[mid]):
                occ = mid
                high = mid - 1
            else:
                low = mid + 1
        if(occ < last_occ):
            last_occ = occ
            max_row = i
    
    return max_row

mat = [[0,0,1],[1,1,1], [0,0,1], [0,0,0]]
n, m = 3, 3
res = max_1_row(mat, n, m)
print(res)