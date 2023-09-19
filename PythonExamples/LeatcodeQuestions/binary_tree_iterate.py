from queue import Queue
from typing import Iterable

class TreeNode:
    value = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'[{self.value}]'

class BinaryTree:
    root: TreeNode = None

    def insert(self, value, node: TreeNode = None) -> TreeNode:
        if not self.root:
            self.root = TreeNode(value)
            return self.root
        if not node:
            node = self.root
        if value < node.value:
            if node.left:
                return self.insert(value, node.left)
            else:
                node.left = TreeNode(value)
                return node.left
        else:
            if node.right:
                return self.insert(value, node.right)
            else:
                node.right = TreeNode(value)
                return node.right

    def get_bfs(self) -> Iterable[TreeNode]:
        nodes_queue = Queue()
        layer = 0
        nodes_queue.put((self.root, layer))
        while not nodes_queue.empty():
            node, layer = nodes_queue.get()
            yield node, layer
            if node.left:
                nodes_queue.put((node.left, layer + 1))
            if node.right:
                nodes_queue.put((node.right, layer + 1))

    def get_dfs(self, node: TreeNode = None) -> Iterable[TreeNode]:
        if not node:
            node = self.root
        yield node
        if node.left:
            yield from self.get_dfs(node.left)
        if node.right:
            yield from self.get_dfs(node.right)

    def get_sorted(self, node: TreeNode = None) -> Iterable[TreeNode]:
        if not node:
            node = self.root
        # if it has left branch
        if node.left:
            yield from self.get_sorted(node.left)
        yield node
        # if it has right branch
        if node.right:
            yield from self.get_sorted(node.right)

if __name__ == '__main__':
    """
        5
      3   7
     2 4 6 8
    1       9
    """
    bt = BinaryTree()
    for a in [5, 3, 4, 2, 7, 8, 6, 9, 1]:
        n = bt.insert(a)
        print(n, end='')
    print('\nBFS')
    for n in bt.get_bfs():
        print(f'{n[0]}{n[1]} ', end='')
    print('\nDFS')
    for n in bt.get_dfs():
        print(n, end='')
    print('\nsorted')
    for n in bt.get_sorted():
        print(n, end='')
