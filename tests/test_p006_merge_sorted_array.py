from problems.p006_merge_sorted_array import solution

TEST_CASES = [
    {
        "description": "Standard merge: [1,2,3,0,0,0] + [2,5,6]",
        "run": lambda: solution([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        "expected": [1, 2, 2, 3, 5, 6],
    },
    {
        "description": "Single element, empty second: [1] + []",
        "run": lambda: solution([1], 1, [], 0),
        "expected": [1],
    },
    {
        "description": "Empty first, single second: [0] + [1]",
        "run": lambda: solution([0], 0, [1], 1),
        "expected": [1],
    },
    {
        "description": "Second array all smaller: [4,5,6,0,0,0] + [1,2,3]",
        "run": lambda: solution([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3),
        "expected": [1, 2, 3, 4, 5, 6],
    },
    {
        "description": "Duplicate values: [1,2,3,0,0,0] + [1,2,3]",
        "run": lambda: solution([1, 2, 3, 0, 0, 0], 3, [1, 2, 3], 3),
        "expected": [1, 1, 2, 2, 3, 3],
    },
]
