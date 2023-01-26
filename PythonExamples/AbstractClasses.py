from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    def __init__(self, value: int):
        self.number = value
        print('MyAbstractClass Ctor', self.number)

    @abstractmethod
    def AddOne(self):
        pass

    def AddTwo(self):
        self.number += 2
        print('MyAbstractClass.AddTwo', self.number)


class MyClassA(MyAbstractClass):
    def __init__(self, value: int):
        super().__init__(value)
        # MyAbstractClass.__init__(self,value)
        print('MyClassA Ctor', self.number)

    def AddOne(self):
        self.number += 1
        print('MyClassA.AddOne', self.number)


class MyClassB(MyClassA):
    def __init__(self, value: int):
        super().__init__(value)
        # MyClassA.__init__(self, value)
        print('MyClassB Ctor', self.number)

    def AddTwo(self) -> int:
        self.number += 3
        print('MyClassB.AddTwo', self.number)
        return self.number


c = MyClassB(4)
c.AddOne()
c.AddTwo()
q = c.AddTwo()
