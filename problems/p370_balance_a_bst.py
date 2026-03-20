DESCRIPTION = """
Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree
with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node
never differs by more than 1.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 1 <= Node.val <= 10^5

Examples:
  Input: root = [1, None, 2, None, 3, None, 4]
  Output: [2, 1, 3, None, None, None, 4] (one valid answer)

  Input: root = [2, 1, 3]
  Output: [2, 1, 3]
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
    Balance a BST. Returns inorder traversal of the balanced tree.

    Args:
        root: TreeNode, the root of the BST.

    Returns:
        A list of integers, inorder traversal of balanced tree.
    """
    return None
