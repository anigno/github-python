class SaferObject:
    _freeze = False

    def __setattr__(self, key, value):
        if SaferObject._freeze and not hasattr(self, key):
            return
        object.__setattr__(self, key, value)

    @staticmethod
    def freeze():
        SaferObject._freeze = True

class MyClass(SaferObject):
    def __init__(self):
        self.a = 5
        self.b = 3
        MyClass.freeze()
        pass

myClass = MyClass()
print(myClass.a)
myClass.c = 4
print(myClass.c)


