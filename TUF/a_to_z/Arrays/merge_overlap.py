from typing import List

def merge_overlap(a:List[List[int]])-> List[List[int]]:
    a.sort()
    ans = []
    for i in range(len(a)):
        if not ans or a[i][0] > ans[-1][1]:
            ans.append(a[i]);
        else:
            ans[-1][1] = a[i][1]
    
    return ans

arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
ans = merge_overlap(arr)
for i in range(len(ans)):
    print(f"[{ans[i][0]}, {ans[i][1]}]", end=" ");