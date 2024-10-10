
def reverse_words(s):
    stack = []
    rev = ''
    word = ''

    for i in range(len(s)):
        if(s[i] != ' '):
            word += s[i]
        else:
            stack.append(word)
            word = ''
    stack.append(word)

    for i in range(len(stack)):
        rev += stack.pop()
        rev += ' '
    
    return rev

s = 'this is an amazing program'
rev = reverse_words(s)
print(rev)