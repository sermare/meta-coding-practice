DESCRIPTION = """Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
    Input: head = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
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
