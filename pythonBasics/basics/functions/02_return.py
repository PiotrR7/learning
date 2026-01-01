def addNumbers(a, b, c):
    return a + b + c

def sumListElements(listData):
    if len(listData) == 0:
        print("List is empty")
        return None
    result = 0
    for v in listData:
        result += v
    return result

print(sumListElements([1, 2, 3, 4, 5]))