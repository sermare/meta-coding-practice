DESCRIPTION = """Longest Univalue Path

Given the root of a binary tree, return the length of the longest path where each node
in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between
them.

Example:
    Input: root = [5, 4, 5, 1, 1, None, 5]
    Output: 2
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
