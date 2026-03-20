DESCRIPTION = """Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

The relative order inside both the even and odd groups should remain as it was in the
input.

Example:
    Input: head = [1, 2, 3, 4, 5]
    Output: [1, 3, 5, 2, 4]

Example:
    Input: head = [2, 1, 3, 5, 6, 4, 7]
    Output: [2, 3, 6, 7, 1, 5, 4]
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
