
def merge_overlap(a):
    print(a[2])
    for i in range(1,len(a),1):
        print(a[i], i)
        if(a[i-1][1] >= a[i][0]):
            a[i-1][1] = a[i][1]
            del a[i]
    
    return a

print(merge_overlap([[1,3],[2,6],[8,10],[15,18]]))