from problems.p588_next_greater_element_i import solution

TEST_CASES = [
    {
        "description": "Standard: [4,1,2] in [1,3,4,2]",
        "run": lambda: solution([4, 1, 2], [1, 3, 4, 2]),
        "expected": [-1, 3, -1],
    },
    {
        "description": "Ascending: [2,4] in [1,2,3,4]",
        "run": lambda: solution([2, 4], [1, 2, 3, 4]),
        "expected": [3, -1],
    },
    {
        "description": "Single element subset",
        "run": lambda: solution([1], [1, 2]),
        "expected": [2],
    },
    {
        "description": "No greater elements",
        "run": lambda: solution([3, 2, 1], [3, 2, 1]),
        "expected": [-1, -1, -1],
    },
]
