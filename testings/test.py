import struct

a = struct.pack('ip', 123, 'hello'.encode())
print(a)
b, c = struct.unpack('ip', a)
print(b)
print(c.decode())
