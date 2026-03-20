DESCRIPTION = """Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and
return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should
remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000
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


def solution(head, k):
    return None
