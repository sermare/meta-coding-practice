from problems.p108_min_cost_climbing_stairs import solution

TEST_CASES = [
    {
        "description": "Three steps",
        "run": lambda: solution([10, 15, 20]),
        "expected": 15,
    },
    {
        "description": "Ten steps with varying costs",
        "run": lambda: solution([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),
        "expected": 6,
    },
    {
        "description": "Two steps, pick cheaper",
        "run": lambda: solution([0, 1]),
        "expected": 0,
    },
    {
        "description": "Equal costs",
        "run": lambda: solution([5, 5, 5, 5]),
        "expected": 10,
    },
    {
        "description": "Increasing costs",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": 6,
    },
]
