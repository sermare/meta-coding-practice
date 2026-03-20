from problems.p542_plus_one import solution

TEST_CASES = [
    {
        "description": "Simple increment",
        "run": lambda: solution([1,2,3]),
        "expected": [1, 2, 4],
    },
    {
        "description": "Carry over",
        "run": lambda: solution([9,9,9]),
        "expected": [1, 0, 0, 0],
    },
    {
        "description": "Single digit",
        "run": lambda: solution([0]),
        "expected": [1],
    },
    {
        "description": "Partial carry",
        "run": lambda: solution([1,9,9]),
        "expected": [2, 0, 0],
    },
    {
        "description": "No carry",
        "run": lambda: solution([4,3,2,1]),
        "expected": [4, 3, 2, 2],
    },
]
