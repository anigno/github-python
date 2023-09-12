class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # self.depth = -1

class Solution:
    def __init__(self):
        self.root = TreeNode(5)
        self.known_nodes = []

    def get_lists(self, node: TreeNode) -> list:
        last_depth = -1
        ret_lists = []
        self.known_nodes.append(node)
        while self.known_nodes:
            node: TreeNode = self.known_nodes.pop(0)
            if last_depth != node.depth:
                ret_lists.append([])
                last_depth = node.depth
            ret_lists[len(ret_lists) - 1].append(node)
            if node.left:
                node.left.depth = node.depth + 1
                self.known_nodes.append(node.left)
            if node.right:
                node.right.depth = node.depth + 1
                self.known_nodes.append(node.right)
        return ret_lists

if __name__ == '__main__':
