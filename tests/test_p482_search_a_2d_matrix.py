from problems.p482_search_a_2d_matrix import solution

TEST_CASES = [
    {
        "description": "Found: target=3",
        "run": lambda: solution([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),
        "expected": True,
    },
    {
        "description": "Not found: target=13",
        "run": lambda: solution([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13),
        "expected": False,
    },
    {
        "description": "First element",
        "run": lambda: solution([[1,3,5,7],[10,11,16,20]], 1),
        "expected": True,
    },
    {
        "description": "Last element",
        "run": lambda: solution([[1,3,5,7],[10,11,16,20]], 20),
        "expected": True,
    },
    {
        "description": "Single element found",
        "run": lambda: solution([[5]], 5),
        "expected": True,
    },
]
