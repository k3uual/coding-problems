
def nCr(r, c):
    # (r-1) 
    #     C 
    #     (c-1)
    ans = 1
    for i in range(1, c):
        ans *= (r - i)
        ans //= i

    return ans
def row(n):
    a = [1]
    ans = 1
    for i in range(1, n):
        ans *= (n - i)
        ans //= i
        a.append(ans)
    
    return a
    
def col(n):
    ans_col = []
    for i in range(n + 1):
        ans_col.append(row(i))
    return ans_col

print(nCr(5, 3)) # Prints element present at that particular row and column
print("----------")
print(*row(5))   # Prints entire row of the triangle
print("----------")
ans = col(5)     # Prints entire Pascal's Triangle
for i in range(len(ans)):
    print(*ans[i])