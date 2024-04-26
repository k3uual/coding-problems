
def reverse(a, start, end):
    
    while(start <= end):
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
    
if __name__ == '__main__':
    right = [1, 2, 3, 4, 5, 6, 7]
    left = [1, 2, 3, 4, 5, 6, 7] 
    # here i did not write left = right 
    # cause left will change with right too
    n = 7
    k = 2
    #for right
    reverse(right, n-k, n-1)
    reverse(right, 0, n-k-1)
    reverse(right, 0, n-1)
    print(right)

    

    #for left
    reverse(left, 0, k-1)
    reverse(left, k, n-1)
    reverse(left, 0, n-1)
    print(left)