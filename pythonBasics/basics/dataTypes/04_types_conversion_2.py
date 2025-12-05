listData = [1, 2, 3, 4, 5]

tupleData = tuple(listData)
print(tupleData)

otherList = list(("Ola", 23, 234))
print(otherList)

setData = set(otherList)
print(type(setData))
print(setData)

frozenSetData = frozenset(tupleData)
print(type(frozenSetData))
print(frozenSetData)

tupleData = ( ("Ola", 1234), ("Adam", 5678) )
dictData = dict(tupleData)
print(dictData)