DESCRIPTION = """Largest BST Subtree

Given the root of a binary tree, find the largest subtree which is also a Binary
Search Tree (BST), where the largest means subtree has the largest number of nodes.

A BST is defined as:
  - The left subtree only contains nodes with keys less than the node's key.
  - The right subtree only contains nodes with keys greater than the node's key.
  - Both left and right subtrees must also be BSTs.

Return the number of nodes of the largest BST subtree.

The tree is given as a list in level-order (None for missing nodes).

Example:
    Input: root = [10,5,15,1,8,None,7]
    Output: 3
    Explanation: The subtree rooted at node 5 (with children 1, 8) is the largest BST.
"""


def solution(root):
    return None
