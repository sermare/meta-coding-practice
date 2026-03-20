from problems.p297_contiguous_array import solution

TEST_CASES = [
    {
        "description": "[0,1] -> 2",
        "run": lambda: solution([0, 1]),
        "expected": 2,
    },
    {
        "description": "[0,1,0] -> 2",
        "run": lambda: solution([0, 1, 0]),
        "expected": 2,
    },
    {
        "description": "[0,0,0,1,1,1] -> 6",
        "run": lambda: solution([0, 0, 0, 1, 1, 1]),
        "expected": 6,
    },
    {
        "description": "[0,0,1,0,0,0,1,1] -> 6",
        "run": lambda: solution([0, 0, 1, 0, 0, 0, 1, 1]),
        "expected": 6,
    },
    {
        "description": "[1,1,1] -> 0",
        "run": lambda: solution([1, 1, 1]),
        "expected": 0,
    },
]
