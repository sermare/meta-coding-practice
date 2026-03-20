DESCRIPTION = """Palindrome Linked List

Given the head of a singly linked list, return True if it is a palindrome, or False
otherwise.

Example:
    Input: head = [1, 2, 2, 1]
    Output: True
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
