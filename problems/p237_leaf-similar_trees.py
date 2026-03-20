DESCRIPTION = """Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order. Two binary trees
are considered leaf-similar if their leaf value sequence is the same.

Return True if and only if the two given trees with root nodes root1 and root2 are
leaf-similar.

Example:
    Input: root1 = [3,5,1,6,2,9,8,None,None,7,4], root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
    Output: True
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


def solution(root1, root2):
    return None
