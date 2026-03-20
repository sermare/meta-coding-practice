DESCRIPTION = """
Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child
  pointer points to the next node and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal.

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100

Examples:
  Input: root = [1, 2, 5, 3, 4, None, 6]
  Output: [1, None, 2, None, 3, None, 4, None, 5, None, 6]

  Input: root = []
  Output: []

  Input: root = [0]
  Output: [0]
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
    Flatten a binary tree to a linked list in-place and return as list.

    Args:
        root: TreeNode, the root of the binary tree.

    Returns:
        A list of values in the flattened order.
    """
    return None
