alpha = {
    0 : "A",
    1 : "B",
    2 : "C",
    3 : "D",
    4 : "E"
}

k = 4
for i in range(5):
    strng = "";
    # for k in range(i)
    for j in range(0, i+1):
        strng += alpha[k]
        k -= 1
    k = 4 - i
    print(strng)