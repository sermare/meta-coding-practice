DESCRIPTION = """Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return True if there is a subtree
of root with the same structure and node values of subRoot and False otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of
this node's descendants. The tree tree could also be considered as a subtree of itself.

Example:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: True

    Input: root = [3,4,5,1,2,None,None,None,None,0], subRoot = [4,1,2]
    Output: False

Constraints:
- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4
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


def solution(root, subRoot):
    return None
