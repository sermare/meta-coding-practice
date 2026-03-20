DESCRIPTION = """Kth Smallest Element in a BST

Given the root of a binary search tree and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.

Example:
    Input: root = [3,1,4,None,2], k = 1
    Output: 1

    Input: root = [5,3,6,2,4,None,None,1], k = 3
    Output: 3
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


def solution(root, k):
    return None
