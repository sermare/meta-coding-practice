DESCRIPTION = """
All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node, and an integer k,
return an array of the values of all nodes that have a distance k from the
target node.

You can return the answer in any order.

Constraints:
- The number of nodes in the tree is in the range [1, 500].
- 0 <= Node.val <= 500
- All the values Node.val are unique.
- target is the value of one of the nodes in the tree.
- 0 <= k <= 1000

Examples:
  Input: root = [3,5,1,6,2,0,8,None,None,7,4], target = 5, k = 2
  Output: [7, 4, 1] (any order)

  Input: root = [1], target = 1, k = 3
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


def solution(root, target, k):
    """
    Find all nodes at distance k from the target node.

    Args:
        root: TreeNode, the root of the binary tree.
        target: int, the value of the target node.
        k: int, the distance.

    Returns:
        A list of integers, values of nodes at distance k.
    """
    return None
