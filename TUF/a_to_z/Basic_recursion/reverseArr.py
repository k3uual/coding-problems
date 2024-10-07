lst = [1,2,3,4,5]
rev = [None] * len(lst)

def reverseArr(i, n):
    if(n == -1):
        return
    reverseArr(i + 1, n - 1)
    rev[n] = lst[i]
    print(i, n)

reverseArr(0, 4)

print(rev)
