DESCRIPTION = """
Merge K Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.

Examples:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
  1->4->5
  1->3->4
  2->6
Merging them into one sorted list: 1->1->2->3->4->4->5->6

Input: lists = []
Output: []

Input: lists = [[]]
Output: []
"""


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedlist(lst):
    """Convert a Python list to a linked list."""
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linkedlist_to_list(node):
    """Convert a linked list to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def solution(lists):
    """
    Merge k sorted linked lists into one sorted linked list.

    Args:
        lists: A list of ListNode heads, each representing a sorted linked list.

    Returns:
        The head ListNode of the merged sorted linked list.
    """
    return None
