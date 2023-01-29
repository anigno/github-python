class GenericEvent:
    """
    enable registration (event) and calling (raise) of handlers collections
    """

    def __init__(self, event_descriptor: str = 'NoName'):
        self.event_descriptor = event_descriptor
        self._handlers = []

    def raise_event(self, data: any):
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
