import math

def prime(num):
    mid = math.floor(math.sqrt(num))
    for i in range(2, mid):
        if(num % i == 0):
            return 0
    return 1

if __name__ == '__main__':
    num = 31
    print(prime(num))
