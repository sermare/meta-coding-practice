from problems.p703_peeking_iterator import solution

TEST_CASES = [
    {
        "description": "Basic peek and next operations",
        "run": lambda: solution([1, 2, 3], ["next", "peek", "next"]),
        "expected": None,
    },
    {
        "description": "Multiple peeks without advancing",
        "run": lambda: solution([1, 2], ["peek", "peek", "next"]),
        "expected": None,
    },
    {
        "description": "hasNext returns false at end",
        "run": lambda: solution([1], ["next", "hasNext"]),
        "expected": None,
    },
    {
        "description": "Interleaved peek and next",
        "run": lambda: solution([1, 2, 3, 4], ["peek", "next", "peek", "next"]),
        "expected": None,
    },
]
