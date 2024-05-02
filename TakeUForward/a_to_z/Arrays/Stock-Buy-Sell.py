
def stock(a): 
    Min = float("inf")
    maxPro = 0
    for i in range(len(a)):
        Min = min(Min, a[i])
        maxPro = max(maxPro, a[i] - Min)
    
    return maxPro
a = [7,3,5,6,8,1,7,0]
print(stock(a))