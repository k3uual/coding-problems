
def missing(n, a):
    sum = int(n*(n+1)/2)
    arrSum = 0
    for i in range(n-1):
        arrSum += a[i]
    
    miss = sum - arrSum
    return miss

print(missing(5, [1,2,4,5]))
