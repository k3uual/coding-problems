from typing import List

def rotate_90(a) -> List[List[int]]:
    res = [[]]
    n = len(a)
    
    for i in range(len(a)):
        if(i < len(a)-1):
            res.append([])
        for j in range(len(a[i])):
            res[i].append(a[n-j-1][i])
    
    return(res)

lst = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_90(lst))