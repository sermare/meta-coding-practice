DESCRIPTION = """
Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4]
- -100 <= Node.val <= 100

Examples:
  Input: root = [1,2,3,4,5]
  Output: 3
  Explanation: The longest path is [4,2,1,3] or [5,2,1,3] with length 3.

  Input: root = [1,2]
  Output: 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build a binary tree from a level-order list (None for missing nodes)."""
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
    Find the length of the diameter of the binary tree.

    Args:
        root: TreeNode - the root of the binary tree

    Returns:
        int - the diameter (longest path length in edges between any two nodes)
    """
    return None
