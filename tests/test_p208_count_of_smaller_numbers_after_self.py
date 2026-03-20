from problems.p208_count_of_smaller_numbers_after_self import solution

TEST_CASES = [
    {
        "description": "Standard case: [5,2,6,1]",
        "run": lambda: solution([5, 2, 6, 1]),
        "expected": [2, 1, 1, 0],
    },
    {
        "description": "Already sorted ascending: [1,2,3]",
        "run": lambda: solution([1, 2, 3]),
        "expected": [0, 0, 0],
    },
    {
        "description": "Sorted descending: [3,2,1]",
        "run": lambda: solution([3, 2, 1]),
        "expected": [2, 1, 0],
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": [0],
    },
    {
        "description": "Duplicates: [2,0,1]",
        "run": lambda: solution([2, 0, 1]),
        "expected": [2, 0, 0],
    },
]
