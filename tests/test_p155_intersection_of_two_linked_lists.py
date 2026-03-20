from problems.p155_intersection_of_two_linked_lists import solution, ListNode

def _make_intersection_case(a_vals, b_vals, common_vals):
    """Build two lists that share a common tail."""
    common = None
    for v in reversed(common_vals):
        n = ListNode(v, common)
        common = n
    headA = common
    for v in reversed(a_vals):
        headA = ListNode(v, headA)
    headB = common
    for v in reversed(b_vals):
        headB = ListNode(v, headB)
    return headA, headB, common

TEST_CASES = [
    {
        "description": "Intersecting lists share node 8",
        "run": lambda: (lambda a, b, c: solution(a, b) is c)(*_make_intersection_case([4, 1], [5, 6, 1], [8, 4, 5])),
        "expected": True,
    },
    {
        "description": "No intersection returns None",
        "run": lambda: (lambda a, b, c: solution(a, b))(*_make_intersection_case([2, 6, 4], [1, 5], [])),
        "expected": None,
    },
    {
        "description": "Intersection at first node of common",
        "run": lambda: (lambda a, b, c: solution(a, b) is c)(*_make_intersection_case([], [3], [2, 4])),
        "expected": True,
    },
    {
        "description": "Both single-node same",
        "run": lambda: (lambda a, b, c: solution(a, b) is c)(*_make_intersection_case([], [], [1])),
        "expected": True,
    },
]
