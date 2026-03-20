DESCRIPTION = """Smallest Subtree with all the Deepest Nodes

Given the root of a binary tree, the depth of each node is the shortest distance to
the root.

Return the smallest subtree such that it contains all the deepest nodes in the original
tree.

A node is called the deepest if it has the largest depth possible among any node in
the entire tree.

Example:
    Input: root = [3,5,1,6,2,0,8,None,None,7,4]
    Output: 2
    Explanation: The deepest nodes are 7 and 4, and their LCA is node 2.
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


def solution(root):
    """Return the value of the root of the smallest subtree containing all deepest nodes."""
    return None
