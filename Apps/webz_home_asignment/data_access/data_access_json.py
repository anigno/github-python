import json
from os import path
from threading import RLock

from Apps.webz_home_asignment.data_access.data_access_base import DataAccessBase

class DataAccessJson(DataAccessBase):
    """saving structured data in json files"""
    _unique_number = 1000
    _locker = RLock()

    @staticmethod
    def _get_unique_number():
        """thread safe unique number generator"""
        with DataAccessJson._locker:
            next_number = DataAccessJson._unique_number
            DataAccessJson._unique_number += 1
            return next_number

    def __init__(self, base_folder: str):
        super().__init__()
        self.base_folder = base_folder

    def open_data_access(self):
        pass

    def close_data_access(self):
        pass

    def save_data(self, prefix: str, data: dict):
        """save dict data to json file
        prefix: saved filename prefix
        data: dictionary with data to save
        """
        file_number = DataAccessJson._get_unique_number()
        file_name = f'{path.join(self.base_folder, prefix)}_{file_number}.json)'
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == '__main__':
    da = DataAccessJson('c:\\temp')
    data = {"person": {"name": "michal", "id": 123456}}
    da.save_data("prefix", data)
    da.save_data("prefix", data)
