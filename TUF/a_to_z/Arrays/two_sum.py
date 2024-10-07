
def two_sum(a, k):
    low = 0
    high = len(a) - 1
    for i in range(len(a)):
        sum = a[low] + a[high]
        if(sum == k):
            return low,high
        elif(sum > k):
            high -= 1
        else:
            low += 1
    return -1,-1

arr = [2,6,5,8,11]
a,b = two_sum(arr, 14)
print(a,b)
