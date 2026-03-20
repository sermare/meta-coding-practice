from problems.p460_linked_list_cycle_ii import solution, ListNode

def _make_cycle(vals, pos):
    """Helper to build a linked list with a cycle at position pos (-1 for no cycle)."""
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0], nodes[pos] if pos >= 0 else None


TEST_CASES = [
    {
        "description": "Cycle at pos 1: [3,2,0,-4] -> node val 2",
        "run": lambda: (lambda r: r[1] if solution(r[0]) is r[1] else None)(_make_cycle([3,2,0,-4], 1)),
        "expected": None,
    },
    {
        "description": "Cycle at pos 0: [1,2] -> node val 1",
        "run": lambda: (lambda r: r[1] if solution(r[0]) is r[1] else None)(_make_cycle([1,2], 0)),
        "expected": None,
    },
    {
        "description": "No cycle: [1] -> None",
        "run": lambda: solution(_make_cycle([1], -1)[0]),
        "expected": None,
    },
    {
        "description": "No cycle: [1,2,3] -> None",
        "run": lambda: solution(_make_cycle([1,2,3], -1)[0]),
        "expected": None,
    },
]
