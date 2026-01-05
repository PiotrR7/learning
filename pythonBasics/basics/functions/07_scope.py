number = 12

def test1():
    print(number)

test1()


def test2():
    number = 100
    print(number)

    if 1 == 1:
        print(number)
        if 2 == 2:
            number = 50
            print(number)
    print(number)

test2()
print(number)

print("\ntest3")
def test3():
    global number
    number = 5
    print("test 3: ", number)

    if 1 == 1:
        number = 6
        print(number)

test3()
print("global number: ", number)