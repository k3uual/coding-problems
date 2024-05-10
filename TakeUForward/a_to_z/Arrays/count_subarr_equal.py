
def count_subarr(a, n, k):
    if(n == 0):
        return 0
    if(n == 1):
        if(a[0] == k):
            return 1
        return 0
    
    j = 1
    i = 0
    sum = a[0] + a[1]
    count = 0
    while(j < n and i <= j):
        if(sum < k):
            j += 1
            if(j == n):
                return count
            sum += a[j]
        if(sum > k):
            sum -= a[i]
            i += 1
        print(i, j, sum)
        if(sum == k):
            sum -= a[i]
            i += 1
            count += 1
    return count

a = [1,1,1]
print(count_subarr(a, len(a), 2))