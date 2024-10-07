
def k_2sorted(a, b, m, n, k):
    if m > n:
        k_2sorted(b, a, n, m, k)
    
    left = k
    low = max(0, k-n)
    high = min(k, m)

    while(high >= low):
        mid1 = (high + low)//2
        mid2 = left - mid1
        
        l1 = float("-inf")
        l2 = float("-inf")
        r1 = float("inf")
        r2 = float("inf")

        if m > mid1:
            r1 = a[mid1]
        if n > mid1:
            r2 = b[mid2]
        if 0 <= mid1 - 1:
            l1 = a[mid1 - 1]
        if 0 <= mid2 - 1:
            l2 = b[mid2 - 1]
        
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    
    return 0

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
print("The k-th element of two sorted arrays is:", k_2sorted(a, b, len(a), len(b), 5))