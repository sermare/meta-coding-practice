DESCRIPTION = """Unique Binary Search Trees II

Given an integer n, return all the structurally unique BSTs (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Return the trees as lists of level-order traversals.

Example:
    Input: n = 3
    Output: 5 trees (return count for simplicity)

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


def solution(n):
    return None
