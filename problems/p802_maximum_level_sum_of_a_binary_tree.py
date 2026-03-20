DESCRIPTION = """Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its
children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at
level x is maximal.

Example:
    Input: root = [1, 7, 0, 7, -8, None, None]
    Output: 2
    Explanation: Level 1 sum = 1, Level 2 sum = 7 + 0 = 7, Level 3 sum = 7 + (-8) = -1.
                 So we return level 2 with maximum sum 7.

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
    return None
