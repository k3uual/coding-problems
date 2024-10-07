
def set_0(a):
    d = []
    i = 0

    for row in range(len(a)):
        for col in range(len(a[row])):
            if(a[row][col] == 0):
                d.append([])
                d[i].append(row)
                d[i].append(col)
                i += 1
    
    for row, col in d:
        for i in range(len(a[row])):
            a[row][i] = 0
        
        for i in range(len(a)):
            a[i][col] = 0

matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
set_0(matrix)
print(matrix)