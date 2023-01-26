import struct
import zlib



def compactString(string: str) -> (int, str):
    mapped = map(ord, string)
    stringBytes = bytearray(mapped)
    compressedString = zlib.compress(stringBytes, 9)
    if len(compressedString) > len(string):
        return string
    return compressedString



def unCompactString(compactedString: str) -> str:
    if isinstance(compactedString,str):
        return compactedString
    string = zlib.decompress(compactedString)
    return string



# s='This is a very long string.........'
s='This is a very long string..........'

a = compactString(s)
b = unCompactString(a)
print(len(s), len(a), len(b))



a=123
b=12.3
c='hello'

print(type(a))
print(type(b))
print(type(c))

ba=bytearray()
sa=str(a)
sb=str(b)
ma=map(ord,sa)
mb=map(ord,sb)
mc=map(ord,c)
ba.extend(ma)
ba.extend(mb)
ba.extend(mc)

print(ba,len(ba),ba.hex())



bs = bytes(s, 'utf-8')
packed=struct.pack("I%ds" % (len(bs),), len(bs), bs)
print(packed)

s=s+s+s
bs = bytes(s, 'utf-8')
pattern= "I%ds%dI" % (len(bs),3)
# pattern= "I{}s3I".format(len(bs))
print(pattern)

packed=struct.pack(pattern, len(bs), bs,1,2,3)
print(packed)
unPacked=struct.unpack(pattern,packed)
print(unPacked)


