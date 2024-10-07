def oneToNandBack(i, n):
    print(i)
    if(i == n):
        return
    oneToNandBack(i + 1, n)
    if(i == n-1):
        print(10)
    print(i)
    

oneToNandBack(1, 10)
