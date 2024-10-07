
def nDiv3_times(a):
    ans = []
    ele1, ele2 = a[0], a[1]
    cnt1, cnt2 = 0, 0
    n = len(a)
    for i in range(2,n):
        if(ele1 == a[i]):
            cnt1 += 1
        elif(ele2 == a[i]):
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
            if(cnt1 == 0):
                cnt1 = 1
                ele1 = a[i]
            elif(cnt2 == 0):
                cnt2 = 1
                ele2 = a[i]

    cnt1, cnt2 = 0, 0
    for i in range(n):
        if ele1 == a[i]:
            cnt1 += 1
        elif ele2 == a[i]:
            cnt2 += 1

    min = n//3 + 1
    if(cnt1 >= min):
        ans.append(ele1)
    if(cnt2 >= min):
        ans.append(ele2)
    
    return ans

print(nDiv3_times([11,22,11,22,22,11]))