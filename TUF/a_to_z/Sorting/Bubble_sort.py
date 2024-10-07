
def bubble_sort(a):
    
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    
a = [13,46,24,52,20,9]
print(a)
bubble_sort(a)
print(a)