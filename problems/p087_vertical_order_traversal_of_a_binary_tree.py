DESCRIPTION = """Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, calculate the vertical order traversal of the
binary tree.

For each node at position (row, col), its left and right children will be at
positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of
the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings
for each column index starting from the leftmost column and ending on the rightmost
column. There may be multiple nodes in the same row and same column. In such a case,
sort these nodes by their values.

Return the vertical order traversal of the binary tree.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]

Example 2:
    Input: root = [1,2,3,4,5,6,7]
    Output: [[4],[2],[1,5,6],[3],[7]]

Example 3:
    Input: root = [1,2,3,4,6,5,7]
    Output: [[4],[2],[1,5,6],[3],[7]]

Constraints:
    - The number of nodes in the tree is in the range [1, 1000].
    - 0 <= Node.val <= 1000
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
