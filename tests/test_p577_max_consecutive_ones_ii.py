from problems.p577_max_consecutive_ones_ii import solution

TEST_CASES = [
    {
        "description": "Flip first zero: [1,0,1,1,0] -> 4",
        "run": lambda: solution([1, 0, 1, 1, 0]),
        "expected": 4,
    },
    {
        "description": "Flip middle: [1,0,1,1,0,1] -> 4",
        "run": lambda: solution([1, 0, 1, 1, 0, 1]),
        "expected": 4,
    },
    {
        "description": "All ones: no flip needed",
        "run": lambda: solution([1, 1, 1, 1]),
        "expected": 4,
    },
    {
        "description": "All zeros: flip one",
        "run": lambda: solution([0, 0, 0]),
        "expected": 1,
    },
    {
        "description": "Single element",
        "run": lambda: solution([0]),
        "expected": 1,
    },
]
