
def max1(a):
    maxi,count = 0,0
    for i in range(len(a)):
        if a[i]:
            count += 1
        else:
            count = 0
        maxi = max(maxi, count)
    return maxi

print(max1([1, 0, 1, 1, 0, 1]))