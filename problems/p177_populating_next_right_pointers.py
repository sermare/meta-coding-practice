DESCRIPTION = """Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and
every parent has two children. Populate each next pointer to point to its next
right node. If there is no next right node, the next pointer should be set to
None.

For this problem, solution takes a level-order list, builds the tree, connects
next pointers, and returns a list of lists showing each level's connections.

Example:
    Input: root = [1,2,3,4,5,6,7]
    Output: [[1,None],[2,3,None],[4,5,6,7,None]]
"""


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build_tree(values):
    if not values:
        return None
    root = Node(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    return root


def collect_next_pointers(root):
    """Return list of lists; each inner list has vals following next pointers, ending with None."""
    if not root:
        return []
    result = []
    level_start = root
    while level_start:
        level = []
        node = level_start
        while node:
            level.append(node.val)
            node = node.next
        level.append(None)
        result.append(level)
        level_start = level_start.left
    return result


def solution(root):
    return None
