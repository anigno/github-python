import copy
import heapq
from threading import Event, Lock, RLock


class PriorityQueueItem:
    """
    Item that is used by the PriorityQueue to hold priority and data
    """

    def __init__(self, priority: int, data: bytes):
        self.priority = priority
        self.data = data

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f'[{self.priority} {self.data}]'


class PriorytyQueue:
    """
    Queue with priority sorting, based on heapq implementation. thread safe
    """

    def __init__(self, maxPriorityLevels=3):
        self.maxPriorityLevels = maxPriorityLevels
        self.queueList = []
        self.queueLock = RLock()
        self.queueEvent = Event()
        self.queueEvent.clear()

    def enqueue(self, priority: int, data):
        if priority > self.maxPriorityLevels or priority < 1:
            raise ValueError(f'priority level error {priority}')
        item = PriorityQueueItem(priority=priority, data=data)
        with self.queueLock:
            heapq.heappush(self.queueList, item)
        self.queueEvent.set()

    def dequeue(self):
        self.queueEvent.wait()
        with self.queueLock:
            if len(self.queueList) <= 1:
                self.queueEvent.clear()
            ret = heapq.heappop(self.queueList)
            return ret

    def items(self):
        """
        :return: an ordered copy of the items
        """
        with self.queueLock:
            ret = copy.deepcopy(self.queueList)
        return ret


if __name__ == '__main__':
    q = PriorytyQueue(3)
    q.enqueue(2, 'a')
    q.enqueue(1, 'b')
    q.enqueue(2, 'c')
    q.enqueue(2, 'd')
    q.enqueue(1, 'e')
    q.enqueue(2, 'f')

    for item in q.items():
        print(item)
