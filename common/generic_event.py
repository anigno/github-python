from collections import namedtuple

class GenericEvent:
    """
    enable registration (event) and calling (raise) of handlers collections
    """

    def __init__(self, args_type: type, event_descriptor: str = 'NoName'):
        self.args_type = args_type
        self.event_descriptor = event_descriptor
        self._handlers = []

    def raise_event(self, data: any):
        if not type(data) is self.args_type:
            raise Exception(f'event types mismatch. expected type: {self.args_type} but received type: {type(data)}')
        for handler in self._handlers:
            handler(data)

    def register(self, handler):
        self._handlers.append(handler)

    def unregister(self, handler):
        self._handlers.remove(handler)

    def clear(self):
        self._handlers.clear()

    def handlers_count(self) -> int:
        return len(self._handlers)

    def __iadd__(self, other):
        self.register(other)
        return self

    def __isub__(self, other):
        self.unregister(other)
        return self

    def is_registered(self, handler):
        return handler in self._handlers

if __name__ == '__main__':
    class MyEventArgsClass:
        pass

    def event_handler(data: MyEventArgsClass):
        print('event handler', data)

    my_event = GenericEvent(MyEventArgsClass, 'my event descriptor')
    my_event += event_handler
    my_event.raise_event(MyEventArgsClass())
    try:
        my_event.raise_event(123)
    except Exception as ex:
        print('exception:', ex)

    MyEventArgsTuple = namedtuple('MyEventArgsTupleDescriptor', ['param1', 'param2'])

    def event_handler_with_tuple(data: MyEventArgsTuple):
        print('event handler', data)

    my_event = GenericEvent(MyEventArgsTuple, 'my event descriptor')
    my_event += event_handler_with_tuple
    my_event.raise_event(MyEventArgsTuple('param1', 17))
    try:
        my_event.raise_event(123)
    except Exception as ex:
        print('exception:', ex)
