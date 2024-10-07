#this solution is using math

def fnd_usingMath(a):
    sm, sm2 = 0, 0
    n = len(a)
    for i in range(n):
        sm += a[i]
        sm2 += (a[i] * a[i])

    smN = n*(n+1)/2
    sm2N = n*(n+1)*(2*(n)+1)/6
    
    diff = smN - sm
    eq2 = (sm2N - sm2)/diff
    
    x = (diff + eq2)/2
    y = eq2 - x
    return(x, y)

a = [3,5,2,5,4]
miss, repeate = fnd_usingMath(a)
print(miss, "-", repeate)