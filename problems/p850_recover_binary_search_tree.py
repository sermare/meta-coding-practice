DESCRIPTION = """Recover Binary Search Tree

You are given the root of a binary search tree (BST), where the values of
exactly two nodes of the tree were swapped by mistake. Recover the tree
without changing its structure.

Example:
    Input: root = [1, 3, None, None, 2]
    Output: [3, 1, None, None, 2]
    Explanation: 3 and 1 are swapped.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build a binary tree from a level-order list. None represents missing nodes."""
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
