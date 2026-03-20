from problems.p565_stock_price_fluctuation import solution

TEST_CASES = [
    {
        "description": "Basic operations",
        "run": lambda: solution(
            ["update", "update", "current", "maximum", "update", "maximum", "update", "minimum"],
            [[1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
        ),
        "expected": [None, None, 5, 10, None, 5, None, 2],
    },
    {
        "description": "Update corrects old timestamp",
        "run": lambda: solution(
            ["update", "update", "maximum", "minimum"],
            [[1, 10], [1, 5], [], []]
        ),
        "expected": [None, None, 5, 5],
    },
    {
        "description": "Single update",
        "run": lambda: solution(
            ["update", "current", "maximum", "minimum"],
            [[1, 100], [], [], []]
        ),
        "expected": [None, 100, 100, 100],
    },
    {
        "description": "Multiple updates different times",
        "run": lambda: solution(
            ["update", "update", "update", "minimum", "maximum", "current"],
            [[1, 3], [2, 7], [3, 1], [], [], []]
        ),
        "expected": [None, None, None, 1, 7, 1],
    },
]
