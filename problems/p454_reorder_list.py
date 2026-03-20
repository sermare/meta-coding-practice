DESCRIPTION = """Reorder List

You are given the head of a singly linked-list:
L0 -> L1 -> ... -> Ln-1 -> Ln

Reorder the list to be in the following form:
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

You may not modify the values in the list's nodes. Only nodes themselves may
be changed.

Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

Constraints:
    - The number of nodes in the list is in the range [1, 5 * 10^4].
    - 1 <= Node.val <= 1000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked(lst):
    """Convert a Python list to a linked list. Returns head node or None."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_to_list(head):
    """Convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result



def solution(head):
    return None
