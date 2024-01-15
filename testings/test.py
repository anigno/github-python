import struct

a = struct.pack('ip', 123, 'hello'.encode())
print(a)
b, c = struct.unpack('ip', a)
print(b)
print(c.decode())


import json

class SomeData:
    def __init__(self):
        self.name = 'abc'
        self.data = [1, 2, 3]

# Create an instance of the SomeData class
some_data_instance = SomeData()

# Convert the instance to a JSON string
json_string = json.dumps(some_data_instance.__dict__)

print(json_string)
