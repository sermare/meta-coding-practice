from problems.p140_search_a_2d_matrix import solution

TEST_CASES = [
    {
        "description": "Target found",
        "run": lambda: solution([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),
        "expected": True,
    },
    {
        "description": "Target not found",
        "run": lambda: solution([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13),
        "expected": False,
    },
    {
        "description": "Single element found",
        "run": lambda: solution([[1]], 1),
        "expected": True,
    },
    {
        "description": "Single element not found",
        "run": lambda: solution([[1]], 0),
        "expected": False,
    },
    {
        "description": "Target at end of matrix",
        "run": lambda: solution([[1,2],[3,4],[5,6]], 6),
        "expected": True,
    },
]
