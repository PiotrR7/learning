import os

print("current working directory: ", os.getcwd())

files = os.listdir(".")
print(files)

files = os.listdir("../dataTypes")
print(files)