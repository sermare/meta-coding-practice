from problems.p675_menu_combination_sum import solution

TEST_CASES = [
    {
        "description": "Simple exact match",
        "run": lambda: solution([2.00, 3.00, 5.00], 5.00),
        "expected": [[2.00, 3.00], [5.00]],
    },
    {
        "description": "No combination possible",
        "run": lambda: solution([3.00, 7.00], 5.00),
        "expected": [],
    },
    {
        "description": "Single item matches",
        "run": lambda: solution([1.50, 2.50], 2.50),
        "expected": [[2.50]],
    },
    {
        "description": "Reuse allowed: target 4 with [2]",
        "run": lambda: solution([2.00], 4.00),
        "expected": [[2.00, 2.00]],
    },
]
