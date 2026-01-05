from functools import reduce

sum = lambda a, b: a + b
print(sum(10, 20))


def generateLambda(num):
    return lambda a: a* num

doubler = generateLambda(2)
print(doubler(4))


listData = [1,2,3,4,5,6,7,8,9,10]
result = list(map(lambda x: x * 3, listData))
print(result)


result = list(filter(lambda a: a > 1, listData))
print(result)


result = reduce(lambda a, b: a + b, listData)
print(result)