DESCRIPTION = """Serialize and Deserialize BST

Design an algorithm to serialize and deserialize a binary search tree. There is
no restriction on how your serialization/deserialization algorithm should work.
You need to ensure that a BST can be serialized to a string and this string can
be deserialized to the original tree structure.

Implement two functions:
- serialize(root) encodes a BST to a single string.
- deserialize(data) decodes your encoded string back to the tree.

For this problem, solution(values) builds a BST, serializes it, deserializes it,
and returns the in-order traversal.

Example:
    Input: values = [2, 1, 3]
    Output: [1, 2, 3]
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
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def solution(values):
    return None
