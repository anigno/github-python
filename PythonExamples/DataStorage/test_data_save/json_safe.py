import _thread
import json
from abc import ABC, abstractmethod
from threading import RLock
from typing import Union


class PersisterBase(ABC):
    """
    low level persistence provider, the way that the files are saved
    """

    def __init__(self, postfix: str, is_debug_mode):
        self.is_debug_mode = is_debug_mode
        self.postfix = postfix

    @abstractmethod
    def save(self, filename: str, obj: object):
        pass

    @abstractmethod
    def load(self, filename: str):
        pass

    @abstractmethod
    def delete(self, filename: str):
        pass

class JsonSafe(PersisterBase):
    class EmptyClass:
        pass

    def save(self, filename: str, obj: object):
        for key in obj.__dict__:
            if isinstance(obj.__dict__[key], _thread.RLock):
                obj.__dict__[key] = None
        json_string = json.dumps(obj.__dict__)
        with open(filename, 'w') as file:
            file.write(json_string)


    def load(self, filename: str) -> any:
        return self.load_typed(filename, JsonSafe.EmptyClass)

    def load_typed(self, filename: str, resoult_type: type) -> any:
        with open(filename, 'r') as file:
            json_string = file.read()
            d = json.loads(json_string)
            e = resoult_type()
            e.__dict__ = d
            return e

    def delete(self, filename: str):
        pass


if __name__ == '__main__':
    class MyDataClass:
        def __init__(self):
            self.lock = RLock()
            self.some_dict = {}
            for a in range(10, 20):
                self.some_dict[a] = str(a)

    my_data = MyDataClass()
    js = JsonSafe('json', False)
    js.save('my_data.json', my_data)
    my_data2 = js.load('my_data.json')
    pass
