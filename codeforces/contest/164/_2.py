lst = [2,2,2,2]

def beauty(a, n):
    flag = 1
    count = 0
    while(flag != 0 and len(a) != 0):
        arr = a.copy()
        for i in range(1, n-1):
            if(arr[i-1] == arr[i+1]):
                arr[i] = arr[i-1]
                
        for i in range(0, len(arr)-1):
            if(arr[i] != arr[i+1]):
                flag = 0
        a.pop()
        n -= 1
        count += 1

    if(flag):
        return -1
    return count

print(beauty(lst, len(lst)))
