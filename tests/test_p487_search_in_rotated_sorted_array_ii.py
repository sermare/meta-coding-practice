from problems.p487_search_in_rotated_sorted_array_ii import solution

TEST_CASES = [
    {
        "description": "Found: target=0",
        "run": lambda: solution([2,5,6,0,0,1,2], 0),
        "expected": True,
    },
    {
        "description": "Not found: target=3",
        "run": lambda: solution([2,5,6,0,0,1,2], 3),
        "expected": False,
    },
    {
        "description": "All same found",
        "run": lambda: solution([1,1,1,1], 1),
        "expected": True,
    },
    {
        "description": "All same not found",
        "run": lambda: solution([1,1,1,1], 2),
        "expected": False,
    },
    {
        "description": "Single element",
        "run": lambda: solution([1], 1),
        "expected": True,
    },
]
