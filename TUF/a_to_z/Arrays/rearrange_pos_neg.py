
def rearrange(a):
    new = [0] * len(a)

    posInd, negInd = 0, 1

    for i in range(len(a)):
        if(a[i] < 0):
            new[negInd] = a[i]
            negInd += 2

        else:
            new[posInd] = a[i]
            posInd += 2
    
    return new

a = [1, 2, 3, -1, -2, -3, -4, -5, 2, 1]    
print(*(rearrange(a)))