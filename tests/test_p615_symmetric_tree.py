from problems.p615_symmetric_tree import solution

TEST_CASES = [
    {
        "description": "Symmetric: [1,2,2,3,4,4,3]",
        "run": lambda: solution([1, 2, 2, 3, 4, 4, 3]),
        "expected": True,
    },
    {
        "description": "Not symmetric: [1,2,2,null,3,null,3]",
        "run": lambda: solution([1, 2, 2, None, 3, None, 3]),
        "expected": False,
    },
    {
        "description": "Single node: [1]",
        "run": lambda: solution([1]),
        "expected": True,
    },
    {
        "description": "Two levels symmetric: [1,2,2]",
        "run": lambda: solution([1, 2, 2]),
        "expected": True,
    },
]
