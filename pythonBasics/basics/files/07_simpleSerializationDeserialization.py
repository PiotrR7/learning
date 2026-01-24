import os
import pickle

scriptDir = os.path.dirname(__file__)

number = 10
listData = ["Jan", "Kowalsky"]
strData = "Jan Kowalsky"

fh = open(scriptDir + "/data.dat", "wb")
pickle.dump(number, fh)
pickle.dump(listData, fh)
pickle.dump(strData, fh)
fh.close()

fh = open(scriptDir + "/data.dat", "rb")
number = pickle.load(fh)
listData = pickle.load(fh)
strData = pickle.load(fh)
fh.close()

print(number)
print(listData)
print(strData)