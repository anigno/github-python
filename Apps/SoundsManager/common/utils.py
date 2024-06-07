import hashlib

def get_hash_code(password: str):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

if __name__ == '__main__':
    print(get_hash_code("1271"))
