DESCRIPTION = """Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference
between the values of any two different nodes in the tree.

Constraints:
- The number of nodes in the tree is in the range [2, 10^4]
- 0 <= Node.val <= 10^5

Example:
    Input: root = [4, 2, 6, 1, 3]
    Output: 1
    Explanation: Minimum difference is between 2 and 3 (or 2 and 1).
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
    return None
