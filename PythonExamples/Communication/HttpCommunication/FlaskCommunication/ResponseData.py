class ResponseData:
    """Data used to build an HTTP response to be delivered from application to service"""

    def __init__(self, key: str, code: str, json):
        self.Key = key
        self.Code = code
        self.Json = json

    def __str__(self):
        return f'[ResponseData[{self.Key}][{self.Code}][{self.Json}]]'
