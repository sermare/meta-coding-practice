from problems.p408_coin_change import solution

TEST_CASES = [
    {
        "description": "Basic: coins=[1,5,10] amount=12",
        "run": lambda: solution([1, 5, 10], 12),
        "expected": 3,
    },
    {
        "description": "Standard: coins=[1,5,10,25] amount=30",
        "run": lambda: solution([1, 5, 10, 25], 30),
        "expected": 2,
    },
    {
        "description": "Impossible: coins=[2] amount=3",
        "run": lambda: solution([2], 3),
        "expected": -1,
    },
    {
        "description": "Zero amount: coins=[1] amount=0",
        "run": lambda: solution([1], 0),
        "expected": 0,
    },
    {
        "description": "Single coin: coins=[1] amount=5",
        "run": lambda: solution([1], 5),
        "expected": 5,
    },
]
