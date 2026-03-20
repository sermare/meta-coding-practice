from problems.p686_reverse_linked_list import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,3,4,5]",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": [5, 4, 3, 2, 1],
    },
    {
        "description": "Two elements: [1,2]",
        "run": lambda: solution([1, 2]),
        "expected": [2, 1],
    },
    {
        "description": "Single element",
        "run": lambda: solution([1]),
        "expected": [1],
    },
    {
        "description": "Empty list",
        "run": lambda: solution([]),
        "expected": [],
    },
]
