DESCRIPTION = """Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of nodes in the tree.

A complete binary tree is one where every level, except possibly the last, is
completely filled, and all nodes in the last level are as far left as possible.

Design an algorithm that runs in less than O(n) time complexity.

Example:
    Input: root = [1,2,3,4,5,6]
    Output: 6

    Input: root = []
    Output: 0
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def solution(root):
    return None
