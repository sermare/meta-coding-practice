DESCRIPTION = """N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values.

N-ary Tree input serialization is represented in their level order traversal, each
group of children is separated by the null value.

For simplicity, the tree is represented as adjacency: a list of (val, [children_vals]).

Example:
    Input: root = [1, [3, 2, 4], [5, 6]]
    (Node 1 has children [3,2,4]; node 3 has children [5,6])
    Output: [[1], [3, 2, 4], [5, 6]]
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []


def build_nary_tree(vals, children_map):
    """Build N-ary tree. children_map maps val -> list of child vals."""
    if not vals:
        return None
    nodes = {v: Node(v) for v in vals}
    for parent_val, child_vals in children_map.items():
        nodes[parent_val].children = [nodes[cv] for cv in child_vals]
    return nodes[vals[0]]


def solution(root):
    return None
