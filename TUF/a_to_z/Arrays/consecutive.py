
def consecutive(a):
    d = set()
    count = 1
    
    for i in range(len(a)):
        d.add(a[i])
    
    for itr in d:
        if itr - 1 not in d:
            cnt = 1
            temp = itr
            
            while temp + 1 in d:
                cnt += 1
                temp += 1
        count = max(count, cnt)

    if(count == 1):
        return 0
    return count

a = [100, 101, 102, 103, 104, 200, 1, 3, 2, 4]
print(consecutive(a))