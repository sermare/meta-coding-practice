DESCRIPTION = """
Problem 19: Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself)."

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the tree.

Examples:
  Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1
  Output: 3
  Explanation: The LCA of nodes 5 and 1 is 3.

  Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4
  Output: 5
  Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
  of itself.

  Input: root = [1,2], p = 1, q = 2
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


def find_node(root, val):
    """Find and return the node with the given value in the tree."""
    if root is None:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)


def solution(root, p, q):
    """
    Find the lowest common ancestor of two nodes in a binary tree.

    Args:
        root: TreeNode, the root of the binary tree.
        p: TreeNode, the first node.
        q: TreeNode, the second node.

    Returns:
        TreeNode, the lowest common ancestor of p and q.
    """
    return None
