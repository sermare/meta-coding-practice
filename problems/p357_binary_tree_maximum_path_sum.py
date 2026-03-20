DESCRIPTION = """
Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
in the sequence has an edge connecting them. A node can only appear in the
sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000

Examples:
  Input: root = [1, 2, 3]
  Output: 6
  Explanation: The optimal path is 2 -> 1 -> 3 with sum 6.

  Input: root = [-10, 9, 20, None, None, 15, 7]
  Output: 42
  Explanation: The optimal path is 15 -> 20 -> 7 with sum 42.
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
    Return the maximum path sum in a binary tree.

    Args:
        root: TreeNode, the root of the binary tree.

    Returns:
        An integer, the maximum path sum.
    """
    return None
