
def rmv_dupli(a):
    i = 0
    
    for j in range(1, len(a)):
        if a[i] != a[j]:
            i += 1
            a[i] = a[j]
    
    return a[:i + 1]

print(rmv_dupli([1,1,1,2,2,3,3,3,3,4,4]))