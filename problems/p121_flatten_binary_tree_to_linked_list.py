DESCRIPTION = """Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child pointer
  points to the next node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example:
    Input: root = [1,2,5,3,4,None,6]
    Output: [1,None,2,None,3,None,4,None,5,None,6]

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100
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


def tree_to_list(root):
    """Convert flattened tree to list by following right pointers."""
    result = []
    while root:
        result.append(root.val)
        result.append(None)
        root = root.right
    return result if result else []


def solution(root):
    """Flatten in-place. Returns None; modifies root."""
    return None
