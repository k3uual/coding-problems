import math
def divisor(num):
    i = 1

    mid = math.floor(math.sqrt(num))
    while(i <= mid):
        if(num%i == 0):
            if(i != num/i):
                print(i)
                print(int(num/i))
            else:
                print(i)
        i += 1

if __name__ == '__main__':
    num = 36
    divisor(num)