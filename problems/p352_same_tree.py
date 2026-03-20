DESCRIPTION = """
Same Tree

Given the roots of two binary trees p and q, write a function to check if they
are the same or not.

Two binary trees are considered the same if they are structurally identical, and
the nodes have the same value.

Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4

Examples:
  Input: p = [1, 2, 3], q = [1, 2, 3]
  Output: True

  Input: p = [1, 2], q = [1, None, 2]
  Output: False

  Input: p = [1, 2, 1], q = [1, 1, 2]
  Output: False
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


def solution(p, q):
    """
    Check if two binary trees are the same.

    Args:
        p: TreeNode, root of the first tree.
        q: TreeNode, root of the second tree.

    Returns:
        Boolean, True if trees are identical.
    """
    return None
