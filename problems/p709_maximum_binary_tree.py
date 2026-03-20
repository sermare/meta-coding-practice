DESCRIPTION = """Maximum Binary Tree

You are given an integer array nums with no duplicates. A maximum binary tree can be
built recursively from nums using the following algorithm:

1. Create a root node whose value is the maximum value in nums.
2. Recursively build the left subtree on the subarray prefix to the left of the
   maximum value.
3. Recursively build the right subtree on the subarray suffix to the right of the
   maximum value.

Return the root of the maximum binary tree. The result should be returned as a
level-order list representation of the tree, using None for missing nodes.

Example:
    Input: nums = [3, 2, 1, 6, 0, 5]
    Output: [6, 3, 5, None, 2, 0, None, None, None, 1]
"""


def solution(nums):
    return None
