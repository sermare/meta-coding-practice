DESCRIPTION = """
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth. The minimum depth is the number of
nodes along the shortest path from the root node down to the nearest leaf node.

A leaf is a node with no children.

Constraints:
- The number of nodes in the tree is in the range [0, 10^5].
- -1000 <= Node.val <= 1000

Examples:
  Input: root = [3, 9, 20, None, None, 15, 7]
  Output: 2

  Input: root = [2, None, 3, None, 4, None, 5, None, 6]
  Output: 5
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
    Return the minimum depth of a binary tree.

    Args:
        root: TreeNode, the root of the binary tree.

    Returns:
        An integer, the minimum depth.
    """
    return None
