
def moveZero(l):
    zero = 0
    end = len(l)
    for i in range(end):
        if(l[i] == 0):
            temp = i
            while(temp < end-1):
                l[temp] = l[temp+1]
                temp += 1
            end -= 1
    while(end < len(l)):
        l[end] = 0
        end += 1

if __name__ == '__main__':
    print(moveZero([1,0,2,3,0,4,0,1]))