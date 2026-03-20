from problems.p492_search_insert_position import solution

TEST_CASES = [
    {
        "description": "Found: target=5 -> 2",
        "run": lambda: solution([1,3,5,6], 5),
        "expected": 2,
    },
    {
        "description": "Insert middle: target=2 -> 1",
        "run": lambda: solution([1,3,5,6], 2),
        "expected": 1,
    },
    {
        "description": "Insert end: target=7 -> 4",
        "run": lambda: solution([1,3,5,6], 7),
        "expected": 4,
    },
    {
        "description": "Insert start: target=0 -> 0",
        "run": lambda: solution([1,3,5,6], 0),
        "expected": 0,
    },
    {
        "description": "Single element insert",
        "run": lambda: solution([1], 0),
        "expected": 0,
    },
]
