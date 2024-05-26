from typing import List

def merge_2sorted(a:List[int], b:List[int])-> List[int]:
    sort = []
    i, j = 0, 0
    while(i < len(a) and j < len(b)):
        if(a[i] < b[j]):
            sort.append(a[i])
            i += 1
        else:
            sort.append(b[j])
            j += 1
    
    for i in range(len(a)):
        sort.append(a[i])
    for j in range(len(b)):
        sort.append(b[j])
    
    i = 0
    while(i < len(sort)):
        for j in range(0, len(a)):
            a[j] = sort[i]
            print(a)
            i += 1
        for k in range(0, len(b)):
            b[k] = sort[i]
            i += 1

arr1 = [1,4,8,10] 
arr2 = [2,3,9]
merge_2sorted(arr1, arr2)
print(arr1, arr2)