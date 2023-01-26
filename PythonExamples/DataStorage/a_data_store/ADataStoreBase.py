from abc import ABC, abstractmethod


class DataStoreBase(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def AddUpdate(self, key: str, value: object) -> bool:
        pass

    @abstractmethod
    def Remove(self, key: str) -> bool:
        pass

    @abstractmethod
    def Save(self) -> bool:
        pass

    @abstractmethod
    def Load(self) -> bool:
        pass

    @abstractmethod
    def __getitem__(self, index):  # []
        pass

    @abstractmethod  # for
    def __iter__(self):
        pass

    @abstractmethod
    def __contains__(self, key):  # in
        pass
