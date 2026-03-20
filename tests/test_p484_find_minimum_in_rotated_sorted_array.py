from problems.p484_find_minimum_in_rotated_sorted_array import solution

TEST_CASES = [
    {
        "description": "Rotated: [3,4,5,1,2] -> 1",
        "run": lambda: solution([3,4,5,1,2]),
        "expected": 1,
    },
    {
        "description": "More rotated: [4,5,6,7,0,1,2] -> 0",
        "run": lambda: solution([4,5,6,7,0,1,2]),
        "expected": 0,
    },
    {
        "description": "Not rotated: [11,13,15,17] -> 11",
        "run": lambda: solution([11,13,15,17]),
        "expected": 11,
    },
    {
        "description": "Two elements: [2,1] -> 1",
        "run": lambda: solution([2,1]),
        "expected": 1,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
]
