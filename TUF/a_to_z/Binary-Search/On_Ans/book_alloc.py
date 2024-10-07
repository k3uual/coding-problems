
def max_sum(a):
    mx = a[0]
    total = 0
    
    for i in a:
        if mx < i:
            mx = i
        total += i
    
    return total, mx

def count_student(a, limit):
    student = 1
    page_stu = a[0]
    
    for i in range(1,len(a)):
        if(a[i] + page_stu > limit):
            student += 1
            page_stu = a[i]
        else:
            page_stu += a[i]
    
    return student

def max_pages(a, stu):
    high, low = max_sum(a)

    while(high >= low):
        mid = (high + low)//2
        mx = count_student(a, mid)

        if(mx > m):
            low = mid + 1
        else:
            high = mid - 1
    
    return low

a = [25, 46, 28, 49, 24] 
m = 4
res = max_pages(a, m)
print(res)