def gcd(a, b):
    print(a,b)
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    a = 4
    b = 8
    print("The GCD of the two numbers is", gcd(96, 14))

