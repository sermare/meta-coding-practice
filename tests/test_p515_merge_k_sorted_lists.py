from problems.p515_merge_k_sorted_lists import solution

TEST_CASES = [
    {
        "description": "Three lists",
        "run": lambda: solution([[1,4,5],[1,3,4],[2,6]]),
        "expected": [1, 1, 2, 3, 4, 4, 5, 6],
    },
    {
        "description": "Empty input",
        "run": lambda: solution([]),
        "expected": [],
    },
    {
        "description": "One empty list",
        "run": lambda: solution([[]]),
        "expected": [],
    },
    {
        "description": "Single list",
        "run": lambda: solution([[1,2,3]]),
        "expected": [1, 2, 3],
    },
    {
        "description": "Two lists",
        "run": lambda: solution([[1,3],[2,4]]),
        "expected": [1, 2, 3, 4],
    },
]
