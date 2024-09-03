
def partion(a, limit):
    painters = 1
    boards = 0
    
    for i in range(len(a)):
        if boards + a[i] <= limit:
            boards += a[i]
        else:
            painters += 1
            boards = a[i]
    
    return painters

def count_boards(a, k):
    high = sum(a)
    low = max(a)

    while(high >= low):
        mid = (high + low)//2
        painters = partion(a, mid)
        if painters > k:
            low = mid + 1
        else:
            high = mid - 1
    
    return low

a = [10, 20, 30, 40]
k = 2
boards = count_boards(a, k)
print(boards)