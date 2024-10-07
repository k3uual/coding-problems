
def more(a):
    count, ele = 0, None
    for i in range(len(a)):
        if(count == 0):
            ele = a[i]
        if(a[i] == ele):
            count += 1
        else:
            count -= 1
    return ele

print(more([2,2,1,1,1,2,2,2,1,1,1,2,2]))