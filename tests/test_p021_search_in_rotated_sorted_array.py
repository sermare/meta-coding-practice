from problems.p021_search_in_rotated_sorted_array import solution

TEST_CASES = [
    {
        "description": "Target 0 found at index 4 in rotated array",
        "run": lambda: solution([4, 5, 6, 7, 0, 1, 2], 0),
        "expected": 4,
    },
    {
        "description": "Target 3 not found in rotated array",
        "run": lambda: solution([4, 5, 6, 7, 0, 1, 2], 3),
        "expected": -1,
    },
    {
        "description": "Target 0 not found in single-element array [1]",
        "run": lambda: solution([1], 0),
        "expected": -1,
    },
    {
        "description": "Target 1 found at index 0 in single-element array [1]",
        "run": lambda: solution([1], 1),
        "expected": 0,
    },
    {
        "description": "Target 3 found at index 0 in two-element rotated array",
        "run": lambda: solution([3, 1], 3),
        "expected": 0,
    },
]
