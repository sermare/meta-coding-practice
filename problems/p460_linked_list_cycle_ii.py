DESCRIPTION = """Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If
there is no cycle, return None.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer.

Do not modify the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: node with value 2 (index 1)
    Explanation: The tail connects to the node at index 1.

Example 2:
    Input: head = [1,2], pos = 0
    Output: node with value 1 (index 0)

Example 3:
    Input: head = [1], pos = -1
    Output: None
    Explanation: There is no cycle in the linked list.

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
