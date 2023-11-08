from ctypes import *

mydll = cdll.LoadLibrary('PythonCppLib.dll')    # x64 dll for x64 python environment
b = mydll.sum(1, 2)
print(b)
mydll.startCalc(1,333333)


