import threading
import types
from abc import ABC



class AEventArgsBase(ABC):
    pass



class SampleEventArgs(AEventArgsBase):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2



class AEvent:
    _eventHandlers = []

    def Raise(self, eventArgs: AEventArgsBase):
        for eventHandler in self._eventHandlers:
            eventHandler(eventArgs)

    def RaiseAsync(self, eventArgs: AEventArgsBase):
        for event in self._eventHandlers:
            threading.Thread(target=event, args=[eventArgs]).start()

    def __iadd__(self, eventHandler):
        if not isinstance(eventHandler, types.FunctionType): raise TypeError(
            '{} {} is not a function'.format(eventHandler, type(eventHandler)))
        self._eventHandlers.append(eventHandler)
        return self

    def __isub__(self, eventHandler):
        if eventHandler in self._eventHandlers:
            self._eventHandlers.remove(eventHandler)
        return self



if __name__ == '__main__':
    def handler_A(a: int):
        print('parameter received:',a)

    OnEvent=AEvent()
    OnEvent+=handler_A

    OnEvent.Raise(1)


    # def handler1(sampleEventArgs):
    #     print('handler 1', sampleEventArgs.value1, sampleEventArgs.value2)
    #
    #
    #
    # def handler2(sampleEventArgs):
    #     print('handler 2', sampleEventArgs.value1, sampleEventArgs.value2)
    #
    #
    #
    # OnEvent = AEvent()
    # OnEvent += handler1
    # OnEvent += handler2
    # OnEvent.Raise(SampleEventArgs(17, 'aaa'))
    # OnEvent.RaiseAsync(SampleEventArgs(56, 'BBB'))

    # OnEvent -= handler2
    # OnEvent -= handler2
    # OnEvent.Raise(17, 'aaa')

    # try:
    #     OnEvent += 'AAABBB'
    # except TypeError as e:
    #     print(e)
    # finally:
    #     pass
