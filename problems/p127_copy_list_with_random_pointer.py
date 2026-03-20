DESCRIPTION = """Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random
pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new
nodes, where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list
such that the pointers in the original list and copied list represent the same list state.

Return the head of the copied linked list.

Example:
    Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Constraints:
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random is null or is pointing to some node in the linked list.
"""


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def build_list(pairs):
    """Build linked list from list of [val, random_index] pairs."""
    if not pairs:
        return None
    nodes = [Node(p[0]) for p in pairs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, p in enumerate(pairs):
        if p[1] is not None:
            nodes[i].random = nodes[p[1]]
    return nodes[0]


def list_to_pairs(head):
    """Convert linked list back to [val, random_index] pairs."""
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    node_to_idx = {id(n): i for i, n in enumerate(nodes)}
    result = []
    for n in nodes:
        rand_idx = node_to_idx[id(n.random)] if n.random else None
        result.append([n.val, rand_idx])
    return result


def solution(head):
    return None
