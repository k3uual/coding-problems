
def find_union(arr1, arr2):
    freq = {}
    union = []
    
    for num in arr1:
        freq[num] = freq.get(num, 0) 
    
    print(freq)
    
    for num in arr2:
        freq[num] = freq.get(num, 0) 
    
    print(freq)
    
    for n in freq:
        union.append(n)
    
    return union

arr1 = [1, 2, 3, 4, 5, 6, 8, 9, 10]
arr2 = [2, 3, 4, 4, 7, 11, 12]

union = find_union(arr1, arr2)

print("Union of arr1 and arr2 is:")
for num in union:
    print(num, end=" ")

