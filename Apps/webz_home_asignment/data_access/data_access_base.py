from abc import ABC, abstractmethod

class DataAccessBase(ABC):
    """base class for data saving"""
    def __init__(self):
        pass

    @abstractmethod
    def open_data_access(self):
        pass

    @abstractmethod
    def close_data_access(self):
        pass

    @abstractmethod
    def save_data(self, prefix: str, data: dict):
        pass
