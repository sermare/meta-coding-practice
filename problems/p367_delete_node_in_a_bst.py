DESCRIPTION = """
Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given
key in the BST. Return the root node reference (possibly updated) of the BST.

The deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- Each node has a unique value.
- root is a valid binary search tree.
- -10^5 <= key <= 10^5

Examples:
  Input: root = [5,3,6,2,4,None,7], key = 3
  Output: [5,4,6,2,None,None,7] (one valid answer)

  Input: root = [5,3,6,2,4,None,7], key = 0
  Output: [5,3,6,2,4,None,7]

  Input: root = [], key = 0
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


def solution(root, key):
    """
    Delete a node with the given key from a BST. Returns inorder traversal.

    Args:
        root: TreeNode, the root of the BST.
        key: int, the value to delete.

    Returns:
        A list of integers, inorder traversal after deletion.
    """
    return None
