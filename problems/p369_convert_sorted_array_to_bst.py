DESCRIPTION = """
Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two
subtrees of every node never differs by more than one.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in strictly increasing order.

Examples:
  Input: nums = [-10, -3, 0, 5, 9]
  Output: [0, -3, 9, -10, None, 5] (one valid answer)

  Input: nums = [1, 3]
  Output: [3, 1] or [1, None, 3]
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


def solution(nums):
    """
    Convert a sorted array to a height-balanced BST. Returns inorder traversal.

    Args:
        nums: List[int], sorted array.

    Returns:
        A list of integers, inorder traversal (should equal input).
    """
    return None
