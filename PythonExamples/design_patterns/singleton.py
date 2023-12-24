class _SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonClass1(metaclass=_SingletonMeta):

    def __init__(self):
        self.some_data = f'hello'

class SingletonClass2(metaclass=_SingletonMeta):
    _counter = 0

    def __init__(self):
        self.some_data = f'hello'

if __name__ == '__main__':
    s1 = SingletonClass1()
    s2 = SingletonClass1()
    s3 = SingletonClass2()
    s4 = SingletonClass2()
    print(s1.some_data)
    print(s2.some_data)
    s1.some_data = 'world'
    print(s1.some_data)
    print(s2.some_data)
    print(s3.some_data)
    print(s4.some_data)
