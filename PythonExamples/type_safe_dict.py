class TypeSafeDict(dict):
    def __init__(self, type, **kwargs):
        super().__init__(**kwargs)
        self.type = type

    def __setitem__(self, key, value):
        if type(value) != self.type:
            raise TypeError(f'Expected type: {self.type} but given: {type(value)}')
        super().__setitem__(key, value)

    def update(self, E=None, **F):
        if E.type != self.type:
            raise TypeError(f'Expected type: {self.type} but given: {type(E.type)}')
        super().update(E)


if __name__ == '__main__':
    class classA:
        def __init__(self, var):
            self.var = var

        def __repr__(self):
            return f'var={self.var}'


    class classB:
        def __init__(self, var):
            self.var = var

        def __repr__(self):
            return f'var={self.var}'


    tsDict1 = TypeSafeDict(classA)
    tsDict1[1] = classA(10)
    tsDict1[2] = classA(20)
    try:
        tsDict1[3]=classB
    except TypeError as ex:
        print(ex)

    print(tsDict1)

    tsDict2 = TypeSafeDict(classA)
    tsDict2[1] = classA(30)

    tsDict1.update(tsDict2)

    print(tsDict1)
