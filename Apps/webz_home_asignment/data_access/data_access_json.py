from Apps.webz_home_asignment.data_access.data_access_base import DataAccessBase

class DataAccessJson(DataAccessBase):
    """saving structured data in json files"""

    def __init__(self, filename: str):
        super().__init__()
        self.filename = filename

    def open_data_access(self):
        pass

    def close_data_access(self):
        pass

    def save_data(self, data: dict):
        pass
