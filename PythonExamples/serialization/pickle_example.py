import pickle

class ClassB:
    def __init__(self):
        self.e = 456

class ClassC:
    def __init__(self):
        self.f = 789

class ClassA(ClassB):
    def __init__(self):
        super().__init__()
        self.a = 123
        self.b = 'hello'
        self.c = {1: 111, 2: 'bbb'}
        self.d = [111, 222, 333]
        self.g = ClassC()

    def serialize_obj(obj):
        if isinstance(obj, (ClassA, ClassB, ClassC)):
            return obj.__dict__
        return obj

c = ClassA()
data = pickle.dumps(c)
c2 = pickle.loads(data)
print(data)
print(c2.b)
