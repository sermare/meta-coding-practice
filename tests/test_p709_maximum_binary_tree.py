from problems.p709_maximum_binary_tree import solution

TEST_CASES = [
    {
        "description": "Basic case: [3,2,1,6,0,5]",
        "run": lambda: solution([3, 2, 1, 6, 0, 5]),
        "expected": [6, 3, 5, None, 2, 0, None, None, None, 1],
    },
    {
        "description": "Sorted ascending: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": [3, 2, None, 1],
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": [1],
    },
    {
        "description": "Two elements: [2,1]",
        "run": lambda: solution([2, 1]),
        "expected": [2, None, 1],
    },
]
