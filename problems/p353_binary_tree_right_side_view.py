DESCRIPTION = """
Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side
of it. Return the values of the nodes you can see ordered from top to bottom.

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Examples:
  Input: root = [1, 2, 3, None, 5, None, 4]
  Output: [1, 3, 4]

  Input: root = [1, None, 3]
  Output: [1, 3]

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
    Return the right side view of a binary tree.

    Args:
        root: TreeNode, the root of the binary tree.

    Returns:
        A list of integers visible from the right side.
    """
    return None
