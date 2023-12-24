class _InstanceCounterMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = 0
        cls._instances[cls] += 1
        instance = super().__call__(*args, **kwargs)
        return instance

    def get_instances(cls):
        return cls._instances[cls]

class InstanceCounter(metaclass=_InstanceCounterMeta):
    def __del__(self):
        print(self, '__del__')

class ClassA(InstanceCounter):
    pass

class ClassB(InstanceCounter):
    pass

if __name__ == '__main__':
    a1 = ClassA()
    a2 = ClassA()
    a3 = ClassA()
    b1 = ClassB()
    b2 = ClassB()
    print(ClassA.get_instances())
    print(ClassB.get_instances())
