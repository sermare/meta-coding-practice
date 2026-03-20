from problems.p202_majority_element import solution

TEST_CASES = [
    {
        "description": "Simple majority: [3,2,3]",
        "run": lambda: solution([3, 2, 3]),
        "expected": 3,
    },
    {
        "description": "Longer array: [2,2,1,1,1,2,2]",
        "run": lambda: solution([2, 2, 1, 1, 1, 2, 2]),
        "expected": 2,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "All same: [5,5,5]",
        "run": lambda: solution([5, 5, 5]),
        "expected": 5,
    },
    {
        "description": "Two elements: [1,1,2]",
        "run": lambda: solution([1, 1, 2]),
        "expected": 1,
    },
]
