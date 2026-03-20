DESCRIPTION = """
Path Sum II

Given the root of a binary tree and an integer targetSum, return all
root-to-leaf paths where the sum of the node values in the path equals
targetSum. Each path should be returned as a list of the node values.

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

Examples:
  Input: root = [5,4,8,11,None,13,4,7,2,None,None,5,1], targetSum = 22
  Output: [[5,4,11,2],[5,8,4,5]]

  Input: root = [1, 2, 3], targetSum = 5
  Output: []

  Input: root = [1, 2], targetSum = 1
  Output: []
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


def solution(root, targetSum):
    """
    Find all root-to-leaf paths with the given sum.

    Args:
        root: TreeNode, the root of the binary tree.
        targetSum: int, the target sum.

    Returns:
        A list of lists of integers representing valid paths.
    """
    return None
