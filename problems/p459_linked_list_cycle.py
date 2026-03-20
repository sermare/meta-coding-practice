DESCRIPTION = """Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle
in it.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, pos is used
to denote the index of the node that tail's next pointer is connected to. Note
that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle, where the tail connects to the 1st node (0-indexed).

Example 2:
    Input: head = [1,2], pos = 0
    Output: true

Example 3:
    Input: head = [1], pos = -1
    Output: false

Constraints:
    - The number of the nodes in the list is in the range [0, 10^4].
    - -10^5 <= Node.val <= 10^5
    - pos is -1 or a valid index in the linked-list.
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
