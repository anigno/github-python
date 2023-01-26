import pickle
from threading import RLock, Thread


class ThreadSafeDict(dict):
    """
    Thread safe dictionary for __setitem__, __getitem__, get
    support with: for locked iteration actions, can be pickled
    """
    DICT_LOCK = '_dict_lock'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._dict_lock = RLock()

    def __setitem__(self, key, value):
        if not hasattr(self, ThreadSafeDict.DICT_LOCK) or self._dict_lock is None:
            self._dict_lock = RLock()
        with self._dict_lock:
            super(ThreadSafeDict, self).__setitem__(key, value)

    def __getitem__(self, item):
        if not hasattr(self, ThreadSafeDict.DICT_LOCK) or self._dict_lock is None:
            self._dict_lock = RLock()
        with self._dict_lock:
            return super(ThreadSafeDict, self).__getitem__(item)

    def get(self, key, default=None):
        if not hasattr(self, ThreadSafeDict.DICT_LOCK) or self._dict_lock is None:
            self._dict_lock = RLock()
        with self._dict_lock:
            return super(ThreadSafeDict, self).get(key, default)

    def __getstate__(self):
        self._dict_lock = None  # pickle will call __getstate__ before starting, remove RLock that couldn't be pickled
        return self

    def __setstate__(self, state):
        if not hasattr(self, ThreadSafeDict.DICT_LOCK) or self._dict_lock is None:
            self._dict_lock = RLock()

    def __enter__(self):
        self._dict_lock.acquire()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._dict_lock.release()


if __name__ == '__main__':

    data = ThreadSafeDict()
    data[0] = 0
    print(data)


    def t1():
        for a in range(1000):
            with data:
                data[0] += 1
        print(data)


    def t2():
        for a in range(1000):
            with data:
                data[0] -= 1
    print(data)

    tr1 = Thread(target=t1)
    tr2 = Thread(target=t2)
    tr1.start()
    tr2.start()
    tr1.join()
    tr2.join()

    print(data)
    data._dict_lock.acquire()
    data._dict_lock.release()

    p = pickle.dumps(data)
    data = pickle.loads(p)

    print(data)
    data._dict_lock.acquire()
    data._dict_lock.release()
