
def kadanes(a):
    sum = 0
    max = float('-inf')
    start, end = -1,-1
    for i in range(len(a)):
        if(sum == 0):
            start = i
        sum += a[i]
        
        if(max < sum):
            max = sum
            end = i
        
        if(sum < 0):
            sum = 0
            
    if(max == 0):
        return []
    return a[start:end+1], max        
    
print(kadanes([-2,1,-3,4,-1,2,1,-5,4]))