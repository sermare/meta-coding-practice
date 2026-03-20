DESCRIPTION = """Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle
in it. There is a cycle if some node in the list can be reached again by
continuously following the next pointer.

Return True if there is a cycle, otherwise return False.

Example:
    Input: head = [3,2,0,-4], pos = 1  (tail connects to node index 1)
    Output: True
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_cycle_list(vals, pos):
    """Create linked list; if pos >= 0 tail.next points to node at index pos."""
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def solution(head):
    return None
