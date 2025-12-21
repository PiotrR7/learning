num = 5
while num > 0:
    print(num)
    num -= 1

num = 0
while True:
    strData = "exit" == input("Wprowadź exit aby zakończyć.")
    if strData:
        break

    num += num + 1
    print("Number value: ", num)