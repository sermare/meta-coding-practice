DESCRIPTION = """Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If
there is no cycle, return None.

Do not modify the linked list.

Example:
    Input: head = [3,2,0,-4], pos = 1
    Output: node at index 1 (value 2)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_cycle_list(vals, pos):
    if not vals:
        return None, None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    cycle_node = None
    if pos >= 0:
        nodes[-1].next = nodes[pos]
        cycle_node = nodes[pos]
    return nodes[0], cycle_node


def solution(head):
    return None
