DESCRIPTION = """
Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path
from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- -10^4 <= Node.val <= 10^4

Examples:
  Input: root = [3, 1, 4, 3, None, 1, 5]
  Output: 4
  Explanation: Root (3), node 3 (left-left), node 4 (right), node 5 (right-right).

  Input: root = [3, 3, None, 4, 2]
  Output: 3

  Input: root = [1]
  Output: 1
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
    Count good nodes in a binary tree.

    Args:
        root: TreeNode, the root of the binary tree.

    Returns:
        An integer, the number of good nodes.
    """
    return None
