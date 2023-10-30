import json

class ConfigReader:
    """provide a weak typed configuration dictionary from a json file"""

    def __init__(self, config_json_filename: str):
        self._config_json_filename = config_json_filename
        self._config_dict: dict = {}
        self._read_config_file()

    def _read_config_file(self):
        """"""
        with open(self._config_json_filename, 'r') as file:
            json_data = file.read()
            self._config_dict = json.loads(json_data)

    @property
    def config_dict(self):
        """returns the configuration dictionary read from config file"""
        return self._config_dict

# none unit test local development testing
if __name__ == '__main__':
    pass
