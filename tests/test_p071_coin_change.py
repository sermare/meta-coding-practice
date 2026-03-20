from problems.p071_coin_change import solution

TEST_CASES = [
    {
        "description": "Standard: coins=[1,2,5] amount=11",
        "run": lambda: solution([1, 2, 5], 11),
        "expected": 3,
    },
    {
        "description": "Impossible: coins=[2] amount=3",
        "run": lambda: solution([2], 3),
        "expected": -1,
    },
    {
        "description": "Zero amount",
        "run": lambda: solution([1], 0),
        "expected": 0,
    },
    {
        "description": "Single coin exact: coins=[1] amount=1",
        "run": lambda: solution([1], 1),
        "expected": 1,
    },
    {
        "description": "Multiple options: coins=[1,3,5] amount=6",
        "run": lambda: solution([1, 3, 5], 6),
        "expected": 2,
    },
]
