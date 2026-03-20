DESCRIPTION = """Maximum Width of Binary Tree

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels. The width of
one level is defined as the length between the end-nodes (the leftmost and
rightmost non-null nodes), where the null nodes between the end-nodes that would
be present in a complete binary tree extending down to that level are also counted.

Example 1:
    Input: root = [1,3,2,5,3,null,9]
    Output: 4
    Explanation: The maximum width exists in the third level with length 4
    (5, 3, null, 9).

Example 2:
    Input: root = [1,3,2,5,null,null,9,6,null,7]
    Output: 7

Example 3:
    Input: root = [1,3,2,5]
    Output: 2

Constraints:
    - The number of nodes in the tree is in the range [1, 3000].
    - -100 <= Node.val <= 100
"""


class TreeNode(object):
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


def solution(root):
    return None
