from problems.p625_search_in_rotated_sorted_array_ii import solution

TEST_CASES = [
    {
        "description": "Target exists: [2,5,6,0,0,1,2] target=0",
        "run": lambda: solution([2, 5, 6, 0, 0, 1, 2], 0),
        "expected": True,
    },
    {
        "description": "Target missing: [2,5,6,0,0,1,2] target=3",
        "run": lambda: solution([2, 5, 6, 0, 0, 1, 2], 3),
        "expected": False,
    },
    {
        "description": "Single element found: [1] target=1",
        "run": lambda: solution([1], 1),
        "expected": True,
    },
    {
        "description": "Single element not found: [1] target=0",
        "run": lambda: solution([1], 0),
        "expected": False,
    },
    {
        "description": "All duplicates: [1,1,1,1] target=1",
        "run": lambda: solution([1, 1, 1, 1], 1),
        "expected": True,
    },
]
