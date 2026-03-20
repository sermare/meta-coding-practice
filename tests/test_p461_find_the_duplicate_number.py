from problems.p461_find_the_duplicate_number import solution

TEST_CASES = [
    {
        "description": "Duplicate 2: [1,3,4,2,2]",
        "run": lambda: solution([1,3,4,2,2]),
        "expected": 2,
    },
    {
        "description": "Duplicate 3: [3,1,3,4,2]",
        "run": lambda: solution([3,1,3,4,2]),
        "expected": 3,
    },
    {
        "description": "All same: [3,3,3,3,3]",
        "run": lambda: solution([3,3,3,3,3]),
        "expected": 3,
    },
    {
        "description": "Duplicate at start: [2,2,2,2,2]",
        "run": lambda: solution([2,2,2,2,2]),
        "expected": 2,
    },
    {
        "description": "Two elements: [1,1]",
        "run": lambda: solution([1,1]),
        "expected": 1,
    },
]
