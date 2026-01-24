import os

scriptDir = os.path.dirname(__file__)
print(scriptDir)

fh = open(scriptDir + "\\ogonki.txt", 'w', encoding = "utf-8")
fh.write("Tekst z ogonkami: ęąśćłó\n")
fh.write("Tekst z ogonkami: ęąśćłó\n")
fh.close()