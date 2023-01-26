class RequestData:
    """Data extracted from the HTTP request to be delivered from service to application"""

    def __init__(self, key: str, method: str, path: str, json):
        self.Key = key
        self.method = method
        self.Path = path
        self.Json = json

    def __str__(self):
        return f'[RequestData[{self.Key}][{self.method}][{self.Path}][{self.Json}]]'
