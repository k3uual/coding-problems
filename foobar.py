
def foobar(n):
    for i in range(1, n):
        if(not(i%5) and not(i%7)):
            print("FooBar")
        elif(not(i%5)):
            print("Foo")
        elif(not(i%7)):
            print("Bar")
        else:
            print(i)

foobar(50)