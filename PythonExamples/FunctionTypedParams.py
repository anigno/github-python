class SomeType:
    pass

def func(a: SomeType, b: str) -> str:
    return str(a)+b

print(func('hello ','aaa'))
print(func(12,' aaa'))


