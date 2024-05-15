
def _4sum(a, n):
    a.sort()
    ans = []
    for i in range(n):
        if(i > 0 and a[i] == a[i-1]):
            continue
        for j in range(i+1, n-1):
            if(j > i+1 and a[j] == a[j-1]):
                continue
            k = j + 1
            l = n - 1
            while(k < l):
                total_sum = a[i] + a[j] + a[k] + a[l]
                if(total_sum < 0):
                    k += 1
                elif(total_sum > 0):
                    l -= 1
                else:
                    ans.append([a[i], a[j], a[k], a[l]])
                    k += 1
                    l -= 1
                    while(k < l and a[k] == a[k-1]):
                        k += 1
                    while(l > k and a[l] == a[l+1]):
                        l -= 1

    return ans

a = [1,0,-1,0,-2,2]
print(_4sum(a, len(a)))