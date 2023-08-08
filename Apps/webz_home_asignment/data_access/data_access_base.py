from abc import ABC, abstractmethod

class DataAccessBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def open_data_access(self):
        pass

    @abstractmethod
    def close_data_access(self):
        pass

    @abstractmethod
    def save_data(self, data: dict):
        pass
