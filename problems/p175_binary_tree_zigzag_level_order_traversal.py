DESCRIPTION = """Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its
nodes' values (i.e., from left to right, then right to left for the next level,
and alternate between).

Example:
    Input: root = [3,9,20,None,None,15,7]
    Output: [[3],[20,9],[15,7]]

    Input: root = [1]
    Output: [[1]]
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
