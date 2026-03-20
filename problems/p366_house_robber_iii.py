DESCRIPTION = """
House Robber III

The thief has found himself a new place for his thievery again. There is only
one entrance to this area, called root. Besides the root, each house has one
and only one parent house. After a tour, the thief realized that all houses
form a binary tree. It will automatically contact the police if two
directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief
can rob without alerting the police.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^4

Examples:
  Input: root = [3, 2, 3, None, 3, None, 1]
  Output: 7
  Explanation: Rob nodes 3 (root) + 3 + 1 = 7.

  Input: root = [3, 4, 5, 1, 3, None, 1]
  Output: 9
  Explanation: Rob nodes 4 + 5 = 9.
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
    Return the maximum amount that can be robbed without alerting police.

    Args:
        root: TreeNode, the root of the binary tree.

    Returns:
        An integer, the maximum robbery amount.
    """
    return None
