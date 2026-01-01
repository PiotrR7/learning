# immutable
def modifyStr(strData):
    strData = "!"
    print(id(strData))

string = "Hello"

modifyStr(string)
print(string)
print(id(string))

# mutable
def modifyList(listData):
    listData.append("World")
    print(id(listData))

list = ["Hello"]

modifyList(list)
print(list)
print(id(list))