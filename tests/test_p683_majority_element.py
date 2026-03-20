from problems.p683_majority_element import solution

TEST_CASES = [
    {
        "description": "Basic: [3,2,3]",
        "run": lambda: solution([3, 2, 3]),
        "expected": 3,
    },
    {
        "description": "Larger array: [2,2,1,1,1,2,2]",
        "run": lambda: solution([2, 2, 1, 1, 1, 2, 2]),
        "expected": 2,
    },
    {
        "description": "Single element",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "All same: [5,5,5]",
        "run": lambda: solution([5, 5, 5]),
        "expected": 5,
    },
]
