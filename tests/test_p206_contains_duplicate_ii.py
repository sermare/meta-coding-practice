from problems.p206_contains_duplicate_ii import solution

TEST_CASES = [
    {
        "description": "Duplicate within range: [1,2,3,1] k=3",
        "run": lambda: solution([1, 2, 3, 1], 3),
        "expected": True,
    },
    {
        "description": "Duplicate at boundary: [1,0,1,1] k=1",
        "run": lambda: solution([1, 0, 1, 1], 1),
        "expected": True,
    },
    {
        "description": "No duplicate in range: [1,2,3,1,2,3] k=2",
        "run": lambda: solution([1, 2, 3, 1, 2, 3], 2),
        "expected": False,
    },
    {
        "description": "No duplicates at all: [1,2,3,4] k=3",
        "run": lambda: solution([1, 2, 3, 4], 3),
        "expected": False,
    },
    {
        "description": "Single element: [1] k=1",
        "run": lambda: solution([1], 1),
        "expected": False,
    },
]
