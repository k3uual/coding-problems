
def sub_xor_k(a, k):
    mpp = {0:1}
    xor = 0
    count = 0
    for i in range(len(a)):
        xor = xor ^ a[i]

        if xor ^ k in mpp:
            count += mpp[xor^k]

        mpp[xor] = mpp.get(xor, 0) + 1
    return count

a = [4, 2, 2, 6, 4]
b = [5, 6, 7, 8, 9]
print(sub_xor_k(a, 6))