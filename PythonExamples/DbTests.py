import io
import pickle

from Decorators import time_measure_function_decorator

data = '123456789_'
someData=''
for i in range(0, 100):
    someData += data

db = dict()
for a in range(0, 100):
    db[a] = dict()
    for b in range(0, 100):
        db[a][b] = someData

print('data db created')

@time_measure_function_decorator
def test01():
    with io.open('d:\\temp\\db_a.txt', 'w', encoding="Latin-1") as f:
        for key, value in db.items():
            pickle.dumps(value)
            # f.write('{0} {1}'.format(key, pickle.dumps(value)))


@time_measure_function_decorator
def test02():
    with io.open('d:\\temp\\db_b.txt', 'wb') as f:
        (pickle.dumps(db))
        # f.write(pickle.dumps(db))


test01()
test02()
