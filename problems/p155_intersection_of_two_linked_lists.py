DESCRIPTION = """Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at
which the two lists intersect. If the two linked lists have no intersection,
return None.

The linked lists must retain their original structure after the function returns.

Example:
    Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], intersection at node 8
    Output: Reference to node with value 8
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


def solution(headA, headB):
    return None
