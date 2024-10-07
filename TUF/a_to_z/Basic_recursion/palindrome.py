s = "123321"

def palindrome(i, n):
    if(i > n):
        return True
    if(s[i] != s[n]):
        return False
    return palindrome(i + 1, n - 1)

print(palindrome(0, len(s) - 1))