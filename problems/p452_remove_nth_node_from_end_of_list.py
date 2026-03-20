DESCRIPTION = """Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Constraints:
    - The number of nodes in the list is sz.
    - 1 <= sz <= 30
    - 0 <= Node.val <= 100
    - 1 <= n <= sz
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



def solution(head, n):
    return None
