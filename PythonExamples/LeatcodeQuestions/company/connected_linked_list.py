import random
from typing import Optional

class LinkedNode:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional[LinkedNode] = None

    def __str__(self):
        return f'[LinkedNode: v={self.value}]'

class LinkedList:
    def __init__(self):
        self.head: Optional[LinkedNode] = None
        self.tail: Optional[LinkedNode] = None

    def append(self, value: int):
        if not self.head:
            self.head = LinkedNode(value)
            self.tail = self.head
            return
        self.tail.next = LinkedNode(value)
        self.tail = self.tail.next

    def __str__(self):
        node = self.head
        s_ret = ''
        while node:
            s_ret += f'{node.value}->'
            node = node.next
        return s_ret + 'N'

def find_connected_node(linked1: LinkedList, linked2: LinkedList) -> Optional[LinkedNode]:
    """create dict from first list, and look for a node from second list in the dict"""
    d = {}
    node = linked1.head
    while node:
        d[node] = node.value
        node = node.next
    node = linked2.head
    while node:
        if node in d:
            return node
        node = node.next
    return None

if __name__ == '__main__':
    linked01 = LinkedList()
    for _ in range(10):
        linked01.append(random.randint(0, 99))
    linked02 = LinkedList()
    for _ in range(10):
        linked02.append(random.randint(0, 99))

    print(linked01)
    print(linked02)
    linked01.head.next.next.next = linked02.head.next.next.next
    print(linked01)
    print(linked02)

    print(find_connected_node(linked01, linked02))
    linked03 = LinkedList()
    print(find_connected_node(linked01, linked03))
