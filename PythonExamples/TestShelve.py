import shelve
import pickle
from Decorators import time_measure_function_decorator

MAX_ITEMS=500

@time_measure_function_decorator
def insertValues():
    for a in range(0, MAX_ITEMS):
        db[str(a)] = [range(a,a+100)]
    db.sync()

@time_measure_function_decorator
def modifyValues():
    for a in range(0, MAX_ITEMS):
        db[str(a)].append(a+2)

@time_measure_function_decorator
def syncValues():
    db.sync()

@time_measure_function_decorator
def checkPickle():
    p=pickle.dumps(db)

db = shelve.open('d:\\temp\\shelveTest\\myShelf', writeback=True)
insertValues()
modifyValues()
syncValues()
checkPickle()
db.close()


