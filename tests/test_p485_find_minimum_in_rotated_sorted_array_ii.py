from problems.p485_find_minimum_in_rotated_sorted_array_ii import solution

TEST_CASES = [
    {
        "description": "No duplicates: [1,3,5] -> 1",
        "run": lambda: solution([1,3,5]),
        "expected": 1,
    },
    {
        "description": "With duplicates: [2,2,2,0,1] -> 0",
        "run": lambda: solution([2,2,2,0,1]),
        "expected": 0,
    },
    {
        "description": "All same: [1,1,1,1] -> 1",
        "run": lambda: solution([1,1,1,1]),
        "expected": 1,
    },
    {
        "description": "Duplicates at edges: [3,3,1,3] -> 1",
        "run": lambda: solution([3,3,1,3]),
        "expected": 1,
    },
    {
        "description": "Single element: [5]",
        "run": lambda: solution([5]),
        "expected": 5,
    },
]
