data = {
    'name' : 'John',
    'age' : 25,
    'city' : 'New York'
}

dataPostalCode = "postalCode"
data[dataPostalCode] = 12345

del data['city']
print(data)
data.clear()
print(data)

data = {
    'name' : 'Kasia',
    'age' : 18,
    'city' : 'New Warsaw',
}
dataCopy = data.copy()
print(dataCopy)
print(data['name'] is dataCopy['name'])
print(data is dataCopy)

data2  = dict.fromkeys(('name','age', 'code'), 0)

print(data2.get('x', "default"))

print("name" in data2)

print(data2.keys())
print(data2.values())