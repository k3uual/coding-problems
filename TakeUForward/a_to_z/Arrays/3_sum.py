
def _3sum(a):
    a.sort()
    i, j, k = 0, len(a)-1, 1
    flag = 0
    ans = []
    
    while(i < j):
        temp = 0 - (a[i] + a[j])
    
        if(a[k] < temp and k < j - 1):
            k += 1
        else:
            print(i, j, k, temp)
            if(a[k] == temp):
                print("---", i, j, k, temp)
                ans.append([a[i], a[k], a[j]])
            if(flag % 2):
                i += 1
                # x = i + 1
                # while(a[i] == a[x]):
                #     i += 1
                #     x += 1
            else:
                # j -= 1
                # x = j - 1
                # while(a[j] == a[x]):
                j -= 1
            k = i + 1
        flag += 1
            
    return ans

print(_3sum([-1,0,1,2,-1,-4]))
# -4, -1, -1, 0, 1, 2