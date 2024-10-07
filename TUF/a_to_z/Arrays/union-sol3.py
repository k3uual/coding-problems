
def find_union(a1, a2):
    i, j = 0, 0  # Pointers
    union = []  # Union list
    n,m = len(a1),len(a2)
    while i < n and j < m:
        if a1[i] <= a2[j]:  
            if len(union) == 0 or union[-1] != a1[i]:
                union.append(a1[i])
            i += 1
        else:  
            if len(union) == 0 or union[-1] != a2[j]:
                union.append(a2[j])
            j += 1

    while i < n:  # If any elements left in a1
        if union[-1] != a1[i]:
            union.append(a1[i])
        i += 1

    while j < m:  # If any elements left in a2
        if union[-1] != a2[j]:
            union.append(a2[j])
        j += 1

    return union


a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(a1, a2)

print("Union of a1 and a2 is:")
print(*union)

