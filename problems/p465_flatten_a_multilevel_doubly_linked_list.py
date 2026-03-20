DESCRIPTION = """Flatten a Multilevel Doubly Linked List

You are given a doubly linked list, which contains nodes that have a next pointer,
a previous pointer, and an additional child pointer. This child pointer may or may
not point to a separate doubly linked list, also containing these special nodes.
These child lists may have one or more children of their own, and so on, to produce
a multilevel data structure.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list. Flatten the list so that all
nodes appear in a single-level doubly linked list. Return the head of the flattened
list. The nodes in the list must have all of their child pointers set to None.

Example 1:
    Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
    Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Example 2:
    Input: head = [1,2,null,3]
    Output: [1,3,2]

Constraints:
    - The number of nodes will not exceed 1000.
    - 1 <= Node.val <= 10^5
"""


class Node(object):
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten_to_list(head):
    """Convert flattened doubly linked list to a Python list of values."""
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result

def solution(head):
    return None
