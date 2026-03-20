DESCRIPTION = """
Binary Search Tree Iterator

Implement the BSTIterator class that represents an iterator over the in-order
traversal of a binary search tree (BST):

- BSTIterator(TreeNode root) Initializes an object with the root of the BST.
- boolean hasNext() Returns true if there is a number in the traversal to the
  right of the pointer.
- int next() Moves the pointer to the right, then returns the number at the pointer.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 0 <= Node.val <= 10^6
- At most 10^5 calls will be made to hasNext, and next.

Examples:
  Input: tree = [7, 3, 15, None, None, 9, 20]
  Operations: next(), next(), hasNext(), next(), hasNext(), next(), hasNext()
  Output: [3, 7, True, 9, True, 15, False]   (after 20 is consumed)
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
    """
    Create a BSTIterator and consume all elements, returning them in order.

    Args:
        root: TreeNode, the root of the BST.

    Returns:
        A list of integers from in-order traversal.
    """
    return None
