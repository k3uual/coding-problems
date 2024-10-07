
def mx_dist(a):
    max_d = 0
    for i in range(1, len(a)):
        if(a[i]-a[i-1] > max_d):
            max_d = a[i] - a[i-1]
    
    return max_d

def mini_max_dist(a):
    high = mx_dist(a)
    low = 0

    while(high - low > pow(10, -6)):
        mid = (high + low)/2.0
        
    