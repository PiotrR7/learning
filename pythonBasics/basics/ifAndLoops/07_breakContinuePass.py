data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in data:
    print(item*2)
    if item == 3:
        break

for item in data:
    print(item)
    if item == 3 or item == 5:
        continue

for item in data:
    pass