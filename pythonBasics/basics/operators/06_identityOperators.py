strData = "test"
print(dir(strData))

print(strData.upper())

a = [1, 2, 3, 4, 5]
b = a

print(a is b)
# True -> więc a i b mają to samo miejsce w pamięci

b.append(6)
print(a is b)

c = [1, 2, 3, 4, 5, 6]

print(b is c)
print(b is not c)