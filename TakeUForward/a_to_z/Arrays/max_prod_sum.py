def max_prod_sum(a):
    mx = 0
    prod = 1
    
    for i in range(len(a)):
        prod *= a[i]
        if(prod > mx):
            mx = prod
        if(prod == 0):
            prod = 1
    
    return mx

a = [1,2,-3,0,-4,-5,-9,0,-50]
mx = max_prod_sum(a)
print(mx)