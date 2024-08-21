cnt = 0
def count(a, low, mid, high):
    left = low
    right = mid + 1
    temp = []
    global cnt

    while(left <= mid and right <= high):
        print("loop1")
        if(a[left] <= a[right]):
            temp.append(a[left])
            left += 1
        else:
            temp.append(a[right])
            cnt += (mid - left) + 1
            right += 1
    
    while(left <= mid):
        print("loop2")
        temp.append(a[left])
        left += 1

    while(right <= high):
        print("loop3")
        temp.append(a[right])
        right += 1

    for i in temp:
        print("loop4")
        a[low] = i
        low += 1
    
def divide(a, low, high):
    if(low >= high):
        return
    mid = (low + high)//2
    divide(a, mid+1, high)
    divide(a, low, mid)
    count(a, low, mid, high)

a = [5,2,3,1,4,9]
divide(a, 0, len(a)-1)
print(cnt)
print(a)