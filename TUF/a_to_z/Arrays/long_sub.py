
def long_sub(a: [int], k: int) -> int:
    sub = 0
    for i in range(len(a)):
        if(a[i] > k):
            break
        sum = a[i]
        count = 1
        j = i + 1
        while(sum <= k and j < len(a)):
            sum += a[j]
            j += 1
            count += 1
            if(sum == k):
                i = j
                sub = max(sub, count)
                break
    return sub

print(long_sub([2,3,5,1,9], 10))
