import time


class Result:
    def __init__(self, success = True, message: str = ''):
        self.Time = time.time()
        self.Success = success
        self.Message = message
