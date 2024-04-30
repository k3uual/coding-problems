
def rearrange(a):
    i,j = 0,1
    while(i <= j and j < len(a)):
        if(i%2 == 1 and a[i] > 0):
            print(a[i], a[j],i,j,"first")
            if(a[j] < 0):
                a[i], a[j] = a[j], a[i]
                print("swap frst", a[i], a[j],i,j)
                i += 1
                j += 1
        elif(i%2 == 0 and a[i] < 0):
            print(a[i], a[j],i,j,"sec")
            if(a[j] > 0):
                a[i], a[j] = a[j], a[i]
                print("swap sec", a[i], a[j],i,j)
                j += 1
                i += 1
        else:
            i += 1
            print("ok", i)
        j += 1    
                    
a = [1,2,3,-1,-2,-3]    
rearrange(a)        
print(a)            