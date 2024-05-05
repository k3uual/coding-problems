
def sub_equal(a, k):
    i, j = 0, 1
    sum = a[0]
    total_sub = 0
    count = 0
    while(j < len(a) and i < len(a)):
        for x in range(i,j+1):
            print(a[x])
        print(count,"---")
        if(sum == k):
            total_sub += 1
        print(total_sub,"<--")
        if(sum < k):
            sum += a[j]
            j += 1
        else:
            sum -= a[i]
            i += 1
        count += 1
    return total_sub

print(sub_equal([3, 1, 2, 4], 6))