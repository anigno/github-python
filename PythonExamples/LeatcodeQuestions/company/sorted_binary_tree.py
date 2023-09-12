import random

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if not self.root:
            self.root = TreeNode(value)
            return
        self._insert_recurse(value, self.root)

    def _insert_recurse(self, value, node):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recurse(value, node.left)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recurse(value, node.right)

    def print_sorted_tree(self):
        self._print_sorted_recurse(self.root)
        print()

    def _print_sorted_recurse(self, node: TreeNode):
        # if leaf
        if not node.left and not node.right:
            self.print_node('LF', node)
            return
        # if it has left branch
        if node.left:
            self._print_sorted_recurse(node.left)
            self.print_node('BL', node)
        else:
            self.print_node('NL', node)
        # if it has right branch
        if node.right:
            self._print_sorted_recurse(node.right)

    def print_node(self, text, node):
        print(f'[{text} {node.value}] ', end='')

if __name__ == '__main__':
    tree = BinaryTree()
    values = [5, 3, 2, 4, 6, 8, 7, 9]
    for v in values:
        tree.insert(v)
    tree.print_sorted_tree()

    tree = BinaryTree()
    for a in range(15):
        v = random.randint(0, 100)
        tree.insert(v)
    tree.print_sorted_tree()
