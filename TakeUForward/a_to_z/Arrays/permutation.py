
def next_permutation(a):
    index = 0
    for i in range(len(a)-2, 0, -1):
        if(a[i] < a[i+1]):
            index = a[i]
            break
    
    if(not index):
        a.reverse()
        return
    
    for i in range(len(a)-2, 0, -1):
        if(a[i] > a[index]):
            a[i], a[index] = a[index], a[i]
            break
    
    j = len(a)-1
    i = index + 1

    while(i < j):
        a[i], a[j] = a[j], a[i]
        j -= 1
        i += 1
    # a[index+1:] = reversed(a[index+1:]) #Above code does the same

b = [5, 4, 3, 2, 1]
a = [2, 1, 5, 4, 3, 0, 0]
next_permutation(a)
print(a)