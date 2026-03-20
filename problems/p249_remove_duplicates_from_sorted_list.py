DESCRIPTION = """Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element
appears only once. Return the linked list sorted as well.

Example:
    Input: head = [1, 1, 2]
    Output: [1, 2]

Example:
    Input: head = [1, 1, 2, 3, 3]
    Output: [1, 2, 3]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def solution(head):
    return None
