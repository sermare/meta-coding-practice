DESCRIPTION = """
Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number (e.g., 1->2->3 = 123).

Return the total sum of all root-to-leaf numbers.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 0 <= Node.val <= 9
- The depth of the tree will not exceed 10.

Examples:
  Input: root = [1, 2, 3]
  Output: 25
  Explanation: 12 + 13 = 25

  Input: root = [4, 9, 0, 5, 1]
  Output: 1026
  Explanation: 495 + 491 + 40 = 1026
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
    Return the total sum of all root-to-leaf numbers.

    Args:
        root: TreeNode, the root of the binary tree.

    Returns:
        An integer, the total sum.
    """
    return None
