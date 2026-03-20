from problems.p156_linked_list_cycle import solution, make_cycle_list

TEST_CASES = [
    {
        "description": "Cycle at pos 1",
        "run": lambda: solution(make_cycle_list([3, 2, 0, -4], 1)),
        "expected": True,
    },
    {
        "description": "Cycle at pos 0 (two nodes)",
        "run": lambda: solution(make_cycle_list([1, 2], 0)),
        "expected": True,
    },
    {
        "description": "No cycle single node",
        "run": lambda: solution(make_cycle_list([1], -1)),
        "expected": False,
    },
    {
        "description": "No cycle multiple nodes",
        "run": lambda: solution(make_cycle_list([1, 2, 3, 4], -1)),
        "expected": False,
    },
]
