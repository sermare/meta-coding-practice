DESCRIPTION = """
Trim a Binary Search Tree

Given the root of a binary search tree and the lowest and highest boundaries
as low and high, trim the tree so that all its elements lie in [low, high].

Trimming the tree should not change the relative structure of the elements that
will remain. Return the root of the trimmed BST. The result's root may change.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^4
- 0 <= low <= high <= 10^4

Examples:
  Input: root = [1, 0, 2], low = 1, high = 2
  Output: [1, None, 2]

  Input: root = [3, 0, 4, None, 2, None, None, 1], low = 1, high = 3
  Output: [3, 2, None, 1]
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


def solution(root, low, high):
    """
    Trim a BST to only include nodes in [low, high]. Returns inorder traversal.

    Args:
        root: TreeNode, the root of the BST.
        low: int, lower boundary.
        high: int, upper boundary.

    Returns:
        A list of integers, inorder traversal of trimmed tree.
    """
    return None
