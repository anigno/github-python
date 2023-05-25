import hashlib

string = "aronanigno136"
hash_object = hashlib.sha256(string.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)

