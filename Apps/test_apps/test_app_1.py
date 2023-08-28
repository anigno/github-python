import hashlib

string = "ronigina"
hash_object = hashlib.sha256(string.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)

