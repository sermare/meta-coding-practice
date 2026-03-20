DESCRIPTION = """Vertical Order Traversal of a Binary Tree

Given the root of a binary tree (as a level-order list), return the vertical order
traversal of its nodes' values.

For each node at position (row, col), its left child is at (row+1, col-1) and its right
child is at (row+1, col+1). The root is at (0, 0).

The vertical order traversal is a list of top-to-bottom orderings for each column index
from left to right. If two nodes are in the same row and column, order them by value.

Example:
    Input: root = [3,9,20,None,None,15,7]
    Output: [[9],[3,15],[20],[7]]

    Input: root = [1,2,3,4,5,6,7]
    Output: [[4],[2],[1,5,6],[3],[7]]
"""


def solution(root):
    return None
