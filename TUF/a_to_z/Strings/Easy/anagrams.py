
def anagrams(s1, s2):
    if(len(s1) != len(s2)): return False

    s1 = s1.upper()
    s2 = s2.upper()
    check = [0 for i in range(26)]

    for i in range(len(s1)):
        check[ord(s1[i])-65] += 1
        check[ord(s2[i])-65] -= 1
    
    for val in check:
        if(val != 0):
            return False
    
    return True

res = anagrams('AAA', 'AAA')
print(res)