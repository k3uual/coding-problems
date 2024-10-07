from typing import List
def spiral(a) -> list[int]:
    top, left = 0, 0
    bottom, right = len(a)-1, len(a[0])-1
    res = []
    
    while(left <= right and top <= bottom):
        #put top
        for i in range(left, right + 1):
            res.append(a[top][i])
        top += 1
        
        #put right 
        for i in range(top, bottom + 1):
            res.append(a[i][right])
        right -= 1
        
        #put bottom
        if(top <= bottom):
            for i in range(right, left -1, -1):
                res.append(a[bottom][i])
            bottom -= 1
        
        #put left
        if(left <= right):
            for i in range(bottom, top - 1, -1):
                res.append(a[i][left])
            left += 1
        
    return res

lst = [ [1, 2, 3, 4],
	    [5, 6, 7, 8],
		[9, 10, 11, 12],
	    [13, 14, 15, 16] 
    ]
print(*spiral(lst))