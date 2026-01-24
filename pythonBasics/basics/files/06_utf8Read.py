import os

scriptDir = os.path.dirname(__file__)

fh = open(scriptDir + "/ogonki.txt", "r", encoding = "utf-8")

while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()