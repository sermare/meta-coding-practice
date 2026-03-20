DESCRIPTION = """
Problem 14: Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes'
values (i.e., from left to right, level by level).

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

Examples:
  Input: root = [3, 9, 20, None, None, 15, 7]
  Output: [[3], [9, 20], [15, 7]]

  Input: root = [1]
  Output: [[1]]

  Input: root = []
  Output: []
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
    """
    Return the level order traversal of a binary tree.

    Args:
        root: TreeNode, the root of the binary tree.

    Returns:
        A list of lists of integers, representing level order traversal.
    """
    return None
