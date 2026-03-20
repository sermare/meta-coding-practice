DESCRIPTION = """Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Example:
    Input: root = [1,2,2,3,4,4,3]
    Output: True

    Input: root = [1,2,2,None,3,None,3]
    Output: False

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
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


def solution(root):
    return None
