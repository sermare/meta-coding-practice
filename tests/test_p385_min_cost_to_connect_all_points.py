from problems.p385_min_cost_to_connect_all_points import solution


TEST_CASES = [
    {
        "description": "Five points: cost 20",
        "run": lambda: solution([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]),
        "expected": 20,
    },
    {
        "description": "Three points: cost 18",
        "run": lambda: solution([[3, 12], [-2, 5], [-4, 1]]),
        "expected": 18,
    },
    {
        "description": "Single point: cost 0",
        "run": lambda: solution([[0, 0]]),
        "expected": 0,
    },
    {
        "description": "Two points",
        "run": lambda: solution([[0, 0], [1, 1]]),
        "expected": 2,
    },
]
