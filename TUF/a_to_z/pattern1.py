num = 5
strng = ""
loop = 2
for i in range(num):
    strng = ""
    for k in range(i, 5):
        strng += " "
    for j in range(i):
        strng += "*"
    for l in range(i, -1, -1):
        strng += "*"
    print(strng)

for i in range(num - 1, 0, -1):
    strng = ""
    for k in range(5, i, -1):
        strng += " "
    for l in range(i, -1, -1):
        strng += "*"
    for j in range(i):
        strng += "*"
    print(strng)
# for i in range(num, -1):
#     strng = ""
#     for k in range(i, 5):
#         strng += " "
#     for j in range(i):
#         strng += str(j)
#     for l in range(i, -1, -1):
#         strng += str(l)

