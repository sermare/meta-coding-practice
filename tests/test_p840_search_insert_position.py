from problems.p840_search_insert_position import solution

TEST_CASES = [
    {
        "description": "Found: [1,3,5,6] target=5",
        "run": lambda: solution([1,3,5,6], 5),
        "expected": 2,
    },
    {
        "description": "Insert in middle: [1,3,5,6] target=2",
        "run": lambda: solution([1,3,5,6], 2),
        "expected": 1,
    },
    {
        "description": "Insert at end: [1,3,5,6] target=7",
        "run": lambda: solution([1,3,5,6], 7),
        "expected": 4,
    },
    {
        "description": "Insert at start: [1,3,5] target=0",
        "run": lambda: solution([1,3,5], 0),
        "expected": 0,
    },
]
