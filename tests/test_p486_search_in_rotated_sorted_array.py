from problems.p486_search_in_rotated_sorted_array import solution

TEST_CASES = [
    {
        "description": "Found in right half: target=0 -> 4",
        "run": lambda: solution([4,5,6,7,0,1,2], 0),
        "expected": 4,
    },
    {
        "description": "Not found: target=3 -> -1",
        "run": lambda: solution([4,5,6,7,0,1,2], 3),
        "expected": -1,
    },
    {
        "description": "Single element not found",
        "run": lambda: solution([1], 0),
        "expected": -1,
    },
    {
        "description": "Found in left half: target=5",
        "run": lambda: solution([4,5,6,7,0,1,2], 5),
        "expected": 1,
    },
    {
        "description": "Not rotated: target=3",
        "run": lambda: solution([1,2,3,4,5], 3),
        "expected": 2,
    },
]
