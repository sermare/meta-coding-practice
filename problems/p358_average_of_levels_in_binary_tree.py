DESCRIPTION = """
Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each
level in the form of an array. Answers within 10^-5 of the actual answer will
be accepted.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

Examples:
  Input: root = [3, 9, 20, None, None, 15, 7]
  Output: [3.0, 14.5, 11.0]

  Input: root = [3, 9, 20, 15, 7]
  Output: [3.0, 14.5, 11.0]
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
    Return the average value of nodes on each level.

    Args:
        root: TreeNode, the root of the binary tree.

    Returns:
        A list of floats, the average at each level.
    """
    return None
