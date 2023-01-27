import random
from math import floor

class HeapList:
    def __init__(self):
        self.heap_list = []

    def push(self, item: any):
        """place item as last and push it up"""
        if not self.heap_list:
            self.heap_list.append(item)
            return
        self.heap_list.append(item)
        self.push_up()

    def pop(self) -> any:
        """return root, place last item in root and push it down"""
        if not self.heap_list:
            return None
        last_item = self.heap_list.pop()
        if not self.heap_list:
            return last_item
        ret = self.heap_list[0]
        self.heap_list[0] = last_item
        self.push_down_recursive(0)
        return ret

    def push_up(self):
        parent = len(self.heap_list) - 1
        while parent > 0:
            child = parent
            parent = floor((child - 1) / 2)
            if self.heap_list[child] > self.heap_list[parent]:
                (self.heap_list[parent], self.heap_list[child]) = (self.heap_list[child], self.heap_list[parent])
            else:
                return

    def push_down_recursive(self, index):
        left = (index + 1) * 2 - 1
        right = (index + 1) * 2
        largest = index
        if len(self.heap_list) > left and self.heap_list[largest] < self.heap_list[left]:
            largest = left
        if len(self.heap_list) > right and self.heap_list[largest] < self.heap_list[right]:
            largest = right
        if largest != index:
            (self.heap_list[index], self.heap_list[largest]) = (self.heap_list[largest], self.heap_list[index])
            self.push_down_recursive(largest)

if __name__ == '__main__':
    heap = HeapList()
    for _ in range(1_000):
        a = random.randint(0, 1_000_000_000)
        heap.push(a)

    print(heap.heap_list)
    item = heap.pop()
    while True:
        prev = item
        item = heap.pop()
        if not item:
            break
        assert item < prev
