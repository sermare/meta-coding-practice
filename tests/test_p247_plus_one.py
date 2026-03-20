from problems.p247_plus_one import solution

TEST_CASES = [
    {
        "description": "Simple increment: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": [1, 2, 4],
    },
    {
        "description": "Carry: [9,9,9]",
        "run": lambda: solution([9, 9, 9]),
        "expected": [1, 0, 0, 0],
    },
    {
        "description": "Single digit: [0]",
        "run": lambda: solution([0]),
        "expected": [1],
    },
    {
        "description": "Partial carry: [1,9,9]",
        "run": lambda: solution([1, 9, 9]),
        "expected": [2, 0, 0],
    },
    {
        "description": "No carry: [4,3,2,1]",
        "run": lambda: solution([4, 3, 2, 1]),
        "expected": [4, 3, 2, 2],
    },
]
