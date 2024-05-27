
def insertion(a):
    for i in range(len(a)):
        temp = a[i]
        j = i - 1
        print(i)
        while(j > 0):
            print(j)
            if(a[j] > temp):
                a[j+1] = a[j]
            else:
                break
            j += 1
        a[j+1] = temp
        
a = [13,46,24,52,20,9]
insertion(a)
print(a)