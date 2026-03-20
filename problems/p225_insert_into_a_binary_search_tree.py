DESCRIPTION = """Insert into a Binary Search Tree

You are given the root node of a BST and a value to insert into the tree. Return the
root node of the BST after the insertion. It is guaranteed that the new value does not
exist in the original BST.

There may exist multiple valid ways of insertion, as long as the tree remains a BST
after insertion.

Example:
    Input: root = [4, 2, 7, 1, 3], val = 5
    Output: [4, 2, 7, 1, 3, 5]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
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


def inorder(root):
    """Return sorted inorder traversal."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def solution(root, val):
    return None
