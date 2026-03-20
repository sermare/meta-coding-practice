from problems.p400_detect_cycles_in_2d_grid import solution


TEST_CASES = [
    {
        "description": "Cycle of 'a' around border",
        "run": lambda: solution([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]),
        "expected": True,
    },
    {
        "description": "Cycle of 'c'",
        "run": lambda: solution([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]),
        "expected": True,
    },
    {
        "description": "No cycle: checkerboard",
        "run": lambda: solution([["a", "b"], ["b", "a"]]),
        "expected": False,
    },
    {
        "description": "Single cell: no cycle",
        "run": lambda: solution([["a"]]),
        "expected": False,
    },
    {
        "description": "All same: cycle exists",
        "run": lambda: solution([["a","a"],["a","a"]]),
        "expected": True,
    },
]
