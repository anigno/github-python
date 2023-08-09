from threading import RLock

class HistoryDictionary:
    """thread safe dictionary to hold urls history"""

    def __init__(self):
        self._locker = RLock()
        self._history_dict: dict[str] = dict()

    def set_item(self, url: str) -> bool:
        """verify url doesn't already exist to add it and return True,
        else return False"""
        with self._locker:
            if url in self._history_dict:
                return False
            self._history_dict[url] = True
            return True
