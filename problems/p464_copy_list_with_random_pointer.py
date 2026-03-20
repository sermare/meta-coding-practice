DESCRIPTION = """Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n
brand new nodes, where each new node has its value set to the value of its
corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the
original list and copied list represent the same list state.

Return the head of the copied linked list.

The linked list is represented as a list of [val, random_index] pairs where
random_index is the index of the node the random pointer points to (0-indexed),
or None if it points to no node.

Example 1:
    Input: head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,None],[13,0],[11,4],[10,2],[1,0]]

Example 2:
    Input: head = [[1,1],[2,1]]
    Output: [[1,1],[2,1]]

Constraints:
    - 0 <= n <= 1000
    - -10^4 <= Node.val <= 10^4
    - Node.random is null or is pointing to some node in the linked list.
"""


class Node(object):
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def build_random_list(pairs):
    """Build a linked list with random pointers from a list of [val, random_index] pairs."""
    if not pairs:
        return None
    nodes = [Node(p[0]) for p in pairs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, p in enumerate(pairs):
        if p[1] is not None:
            nodes[i].random = nodes[p[1]]
    return nodes[0]


def serialize_random_list(head):
    """Serialize a linked list with random pointers to list of [val, random_index]."""
    if not head:
        return []
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    node_to_idx = {id(n): i for i, n in enumerate(nodes)}
    result = []
    for n in nodes:
        ridx = node_to_idx[id(n.random)] if n.random else None
        result.append([n.val, ridx])
    return result

def solution(head):
    return None
