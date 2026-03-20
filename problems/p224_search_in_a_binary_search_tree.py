DESCRIPTION = """Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals val and return the subtree
rooted with that node. If such a node does not exist, return None.

Example:
    Input: root = [4, 2, 7, 1, 3], val = 2
    Output: [2, 1, 3]
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


def tree_to_list(root):
    """Convert tree to level-order list."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return result


def solution(root, val):
    return None
