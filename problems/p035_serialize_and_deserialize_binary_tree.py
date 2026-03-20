DESCRIPTION = """
Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work. You
just need to ensure that a binary tree can be serialized to a string and this
string can be deserialized to the original tree structure.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000

Examples:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
(The tree is serialized and then deserialized back to the same structure.)

Input: root = []
Output: []
"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(values):
    """Build a binary tree from a level-order list (None represents null nodes)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
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


def tree_to_list(root):
    """Convert a binary tree to a level-order list."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


class Codec:
    """Codec class for serializing and deserializing a binary tree."""

    def serialize(self, root):
        """Encodes a tree to a single string.

        Args:
            root: The root TreeNode of the binary tree.

        Returns:
            A string representation of the tree.
        """
        return None

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        Args:
            data: A string representation of the tree.

        Returns:
            The root TreeNode of the reconstructed binary tree.
        """
        return None


# The solution is the Codec class itself.
solution = Codec
