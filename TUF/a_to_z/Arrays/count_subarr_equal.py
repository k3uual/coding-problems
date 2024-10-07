
def count_subarr(a, n, k):
    d = {}
    d[0] = 1
    sum = 0
    count = 0
    
    for i in range(len(a)):
        sum += a[i]
        if(d.get(sum-k)):
            count += d[sum-k]
        d[sum] = d.get(sum, 0) + 1
        
    return count

a = [1,2,3,-3,1,1,1,4,2,-3]

print(count_subarr(a, len(a), 3))