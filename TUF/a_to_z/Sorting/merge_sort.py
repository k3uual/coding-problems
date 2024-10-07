def merge(a, low, high):
    if(low >= high): return

    mid = (low + high)//2
    
    merge(a, low, mid)
    
    merge(a, mid+1, high)
    
    sort(a, low, mid, high)

def sort(a, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    print(a[left:right])
    while(left <= mid and right <= high):
        if(a[right] < a[left]):
            temp.append(a[right])
            right += 1
        else:
            temp.append(a[left])
            left += 1

    while(left <= mid):
        temp.append(a[left])
        left += 1
    while(right <= high):
        temp.append(a[right])
        right += 1
    
    for i in temp:
        a[low] = i
        low += 1
    print(a, "high=", left, "low=", right)

a = [4,2,1,6,7]
merge(a, 0, len(a)-1)
# print(a)