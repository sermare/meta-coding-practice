from problems.p142_majority_element import solution

TEST_CASES = [
    {
        "description": "Simple majority",
        "run": lambda: solution([3, 2, 3]),
        "expected": 3,
    },
    {
        "description": "Longer array",
        "run": lambda: solution([2, 2, 1, 1, 1, 2, 2]),
        "expected": 2,
    },
    {
        "description": "Single element",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "All same",
        "run": lambda: solution([5, 5, 5]),
        "expected": 5,
    },
    {
        "description": "Two elements with majority",
        "run": lambda: solution([1, 1, 2]),
        "expected": 1,
    },
]
