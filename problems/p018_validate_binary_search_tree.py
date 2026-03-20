DESCRIPTION = """
Problem 18: Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree
(BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the
  node's key.
- The right subtree of a node contains only nodes with keys greater than the
  node's key.
- Both the left and right subtrees must also be binary search trees.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

Examples:
  Input: root = [2, 1, 3]
  Output: True

  Input: root = [5, 1, 4, None, None, 3, 6]
  Output: False
  Explanation: The root node's value is 5 but its right child's value is 4.

  Input: root = [1]
  Output: True

  Input: root = []
  Output: True
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
    Determine if the binary tree is a valid BST.

    Args:
        root: TreeNode, the root of the binary tree.

    Returns:
        True if the tree is a valid BST, False otherwise.
    """
    return None
