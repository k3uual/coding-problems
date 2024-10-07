
def selection_sort(a):
    for i in range(len(a)-1):
        mini = i
        for j in range(i,len(a)):
            if(a[mini] > a[j]):
                mini = j
        if(i != mini):
            a[mini], a[i] = a[i], a[mini]

a = [13,46,24,52,20,9]
print(a)
selection_sort(a)
print(a)