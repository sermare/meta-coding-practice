from problems.p320_maximum_gap import solution

TEST_CASES = [
    {
        "description": "Basic: [3,6,9,1] -> 3",
        "run": lambda: solution([3, 6, 9, 1]),
        "expected": 3,
    },
    {
        "description": "Two elements: [10,1] -> 9",
        "run": lambda: solution([10, 1]),
        "expected": 9,
    },
    {
        "description": "Less than 2 elements: [1] -> 0",
        "run": lambda: solution([1]),
        "expected": 0,
    },
    {
        "description": "All same: [1,1,1,1] -> 0",
        "run": lambda: solution([1, 1, 1, 1]),
        "expected": 0,
    },
]
