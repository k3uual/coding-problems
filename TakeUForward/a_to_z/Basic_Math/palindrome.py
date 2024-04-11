def palindrome(check):
    j = len(check) - 1
    i = 0
    while(i < j):
        if(check[i] != check[j]):
            return 0
        i += 1
        j -= 1
    return 1

if __name__ == '__main__':
    num = 123321
    check = str(num)
    print(palindrome(check))