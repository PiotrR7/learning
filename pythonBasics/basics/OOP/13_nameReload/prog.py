import mathModule
import importlib

print(mathModule.addNumbers(10, 2))
print(__name__)

importlib.reload(mathModule)