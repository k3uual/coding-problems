def leader(a, n):
    ans = []
    
    lead = a[n - 1]
    ans.insert(0, lead)
    
    for i in range(n-2, -1, -1):
        if(lead < a[i]):
            lead = a[i]
            ans.insert(0, lead)
    return ans

n = 6
arr = [10, 22, 12, 3, 0, 6]
print(*leader(arr, n))