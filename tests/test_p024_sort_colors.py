from problems.p024_sort_colors import solution

TEST_CASES = [
    {
        "description": "Sort [2,0,2,1,1,0] to [0,0,1,1,2,2]",
        "run": lambda: solution([2, 0, 2, 1, 1, 0]),
        "expected": [0, 0, 1, 1, 2, 2],
    },
    {
        "description": "Sort [2,0,1] to [0,1,2]",
        "run": lambda: solution([2, 0, 1]),
        "expected": [0, 1, 2],
    },
    {
        "description": "Single element [0] stays [0]",
        "run": lambda: solution([0]),
        "expected": [0],
    },
    {
        "description": "Sort [1,2,0,1,2,0] to [0,0,1,1,2,2]",
        "run": lambda: solution([1, 2, 0, 1, 2, 0]),
        "expected": [0, 0, 1, 1, 2, 2],
    },
    {
        "description": "Sort [2,2,2,1,1,0,0] to [0,0,1,1,2,2,2]",
        "run": lambda: solution([2, 2, 2, 1, 1, 0, 0]),
        "expected": [0, 0, 1, 1, 2, 2, 2],
    },
]
