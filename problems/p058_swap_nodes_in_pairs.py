DESCRIPTION = """Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must
solve the problem without modifying the values in the list's nodes (i.e., only
nodes themselves may be changed).

Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

Example 2:
    Input: head = []
    Output: []

Example 3:
    Input: head = [1]
    Output: [1]

Constraints:
    - The number of nodes in the list is in the range [0, 100].
    - 0 <= Node.val <= 100
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def solution(head):
    return None
