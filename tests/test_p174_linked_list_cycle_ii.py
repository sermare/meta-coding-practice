from problems.p174_linked_list_cycle_ii import solution, make_cycle_list

TEST_CASES = [
    {
        "description": "Cycle at pos 1 (val 2)",
        "run": lambda: (lambda h, c: solution(h) is c)(*make_cycle_list([3, 2, 0, -4], 1)),
        "expected": True,
    },
    {
        "description": "Cycle at pos 0",
        "run": lambda: (lambda h, c: solution(h) is c)(*make_cycle_list([1, 2], 0)),
        "expected": True,
    },
    {
        "description": "No cycle returns None",
        "run": lambda: (lambda h, c: solution(h))(*make_cycle_list([1], -1)),
        "expected": None,
    },
    {
        "description": "No cycle longer list",
        "run": lambda: (lambda h, c: solution(h))(*make_cycle_list([1, 2, 3], -1)),
        "expected": None,
    },
]
