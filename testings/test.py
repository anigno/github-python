import struct

a = struct.pack('ip', 123, 'hello'.encode())
print(a)
b, c = struct.unpack('ip', a)
print(b)
print(c.decode())

d = {}
d[1] = 111
d[2] = 333
print(d)
e = d[1]
del (d[1])
print(d)
print(e)
del (e)
print(e)
