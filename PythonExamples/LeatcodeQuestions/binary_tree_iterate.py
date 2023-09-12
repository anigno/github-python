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

    def insert(self, value) -> TreeNode:
        if not self.root:
            self.root = TreeNode(value)
            return self.root
        return BinaryTree._insert_recurse(self.root, value)

    @staticmethod
    def _insert_recurse(node: TreeNode, value) -> TreeNode:
        if value < node.value:
            if node.left:
                return BinaryTree._insert_recurse(node.left, value)
            else:
                node.left = TreeNode(value)
                return node.left
        else:
            if node.right:
                return BinaryTree._insert_recurse(node.right, value)
            else:
                node.right = TreeNode(value)
                return node.right

    def get_bfs_generator(self) -> Iterable[TreeNode]:
        nodes_queue = Queue()
        nodes_queue.put(self.root)
        while not nodes_queue.empty():
            node = nodes_queue.get()
            yield node
            if node.left:
                nodes_queue.put(node.left)
            if node.right:
                nodes_queue.put(node.right)

    def get_dfs_generator(self) -> Iterable[TreeNode]:
        for node in self._dfs_recurse(self.root):
            yield node

    def _dfs_recurse(self, node: TreeNode) -> Iterable[TreeNode]:
        yield node
        if node.left:
            yield from self._dfs_recurse(node.left)
        if node.right:
            yield from self._dfs_recurse(node.right)

    def print_sorted(self, node: TreeNode = None):
        if not node:
            node = self.root
        # if leaf
        if not node.left and not node.right:
            print(node,end='')
            return
        # if it has left branch
        if node.left:
            self.print_sorted(node.left)
            print(node,end='')
        else:
            print(node,end='')
        # if it has right branch
        if node.right:
            self.print_sorted(node.right)

if __name__ == '__main__':
    bt = BinaryTree()
    for a in [5, 3, 4, 2, 7, 8, 6, 9, 1]:
        n = bt.insert(a)
        print(f'inserted {n}',end='')
    print('\nBFS')
    for n in bt.get_bfs_generator():
        print(n,end='')
    print('\nDFS')
    for n in bt.get_dfs_generator():
        print(n,end='')
    print('\nsorted')
    bt.print_sorted()
    print()
