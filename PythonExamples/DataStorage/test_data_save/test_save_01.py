import json
import pickle
import time
from threading import RLock

import jsonpickle

from DataStorage.test_data_save.json_safe import JsonSafe

class MyDataClass:
    def __init__(self):
        # self.lock = RLock()
        self.some_dict = {}
        for b in 'abcdefghijklmnopqrstuvwxyz':
            self.some_dict[b]={}
            for a in range(100, 200):
                self.some_dict[b][a] = str(a)

my_data = MyDataClass()

t0 = time.perf_counter()
json_p = jsonpickle.encode(my_data, unpicklable=False, keys=True)
t1 = time.perf_counter()
with open('my_data.json', 'w') as file_handler:
    file_handler.write(json_p)
t2 = time.perf_counter()
pickle_string = pickle.dumps(my_data)
t3 = time.perf_counter()
with open('my_data.bin', 'wb') as file_handler:
    file_handler.write(pickle_string)
t4 = time.perf_counter()

print(f'{1000*(t1 - t0)} json_p')
print(f'{1000*(t2 - t1)} my_data.json')
print(f'{1000*(t3 - t2)} pickle_string')
print(f'{1000*(t4 - t3)} my_data.bin')

t5 = time.perf_counter()
s1 = json.dumps(my_data.__dict__,)
t6 = time.perf_counter()
print(f'{t6 - t5} json')
with open('my_data2.json', 'w') as file_handler:
    file_handler.write(s1)
d1=json.loads(s1)


