DESCRIPTION = """Delete Node in a Linked List

There is a singly-linked list head. We want to delete a node `node` in it.
You are given the node to be deleted `node`. You will not be given access to
the first node of head.

All the values of the linked list are unique, and it is guaranteed that the
given node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing
it from memory. We mean:
- The value of the given node should not exist in the linked list.
- The number of nodes should decrease by one.

Example:
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
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


def find_node(head, val):
    current = head
    while current:
        if current.val == val:
            return current
        current = current.next
    return None


def solution(node):
    return None
