#repeate and missing using xor
def fnd_usingXOR(a):
    xor = 0

    for i in range(len(a)):
        xor ^= a[i]
        xor ^= (i + 1)

    num = (xor & ~(xor - 1))
    
    zero, one = 0, 0
    
    for i in a:
        if(i & num != 0):
            one ^= i
        else:
            zero ^= i

    for i in range(1, len(a)+1):
        if(i & num != 0):
            one ^= i
        else:
            zero ^= i

    # for i in range(len(a)):
    #     if(a[i] & num != 0):
    #         one ^= a[i]
    #     if(a[i] & num == 0):
    #         zero ^= a[i]
    #     if(i + 1 & num != 0):
    #         one ^= (i + 1)
    #     if(i + 1 & num != 0):
    #         zero ^= (i + 1)

    for i in a:
        if(one == i):
            return(zero, one)
    
    return(one, zero)


a = [3,1,2,5,5]
miss, repeate = fnd_usingXOR(a)
print(miss, "-", repeate)

# 011 101 010 101 100
# 100 011 100 100