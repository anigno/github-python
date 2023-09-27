from sortedcontainers import SortedDict

class TimeStampDictionary:
    """storing key,value and timestamp. if key exist replace timestamp, if timestamp passed remove item"""

    def __init__(self):
        self.data_dict = {}
        self.time_heap = SortedDict()
        self.local_timestamp = 3

    def set(self, key, value, timestamp: float):
        # clean old timestamps
        if self.time_heap:
            t = self.time_heap.peekitem(0)
            while t[0] < self.local_timestamp:
                self.time_heap.pop(t[0])
                self.data_dict.pop(t[1])
                t = self.time_heap.peekitem(0)

        # insert new data
        if key in self.data_dict:
            timestamp_to_remove = self.data_dict[key][1]
            self.time_heap.pop(timestamp_to_remove)
        self.time_heap[timestamp] = key
        self.data_dict[key] = (value, timestamp)

    def get(self, key):
        pass

if __name__ == '__main__':
    data = TimeStampDictionary()
    data.set(5, 55, 10.1)
    data.set(4, 44, 8.1)
    data.set(6, 66, 6.1)
    data.set(4, 444, 9.1)

    print(data.data_dict)
    print(data.time_heap)

    data.local_timestamp = 7
    data.set(7, 77, 11.1)

    print(data.data_dict)
    print(data.time_heap)
