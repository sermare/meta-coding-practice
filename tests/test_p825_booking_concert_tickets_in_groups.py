from problems.p825_booking_concert_tickets_in_groups import solution

TEST_CASES = [
    {
        "description": "Gather 4 from row 0: n=2, m=5",
        "run": lambda: solution(2, 5, [("gather", 4, 0)]),
        "expected": [[0, 0]],
    },
    {
        "description": "Gather then fail: n=2, m=5",
        "run": lambda: solution(2, 5, [("gather", 4, 0), ("gather", 2, 0)]),
        "expected": [[0, 0], []],
    },
    {
        "description": "Scatter within capacity",
        "run": lambda: solution(2, 5, [("gather", 4, 0), ("scatter", 5, 1)]),
        "expected": [[0, 0], True],
    },
    {
        "description": "Scatter exceeds capacity",
        "run": lambda: solution(2, 5, [("gather", 4, 0), ("scatter", 5, 1), ("scatter", 5, 1)]),
        "expected": [[0, 0], True, False],
    },
]
