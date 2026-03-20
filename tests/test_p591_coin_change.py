from problems.p591_coin_change import solution

TEST_CASES = [
    {
        "description": "Standard: coins=[1,5,10,25] amount=30 -> 2",
        "run": lambda: solution([1, 5, 10, 25], 30),
        "expected": 2,
    },
    {
        "description": "Impossible: coins=[2] amount=3 -> -1",
        "run": lambda: solution([2], 3),
        "expected": -1,
    },
    {
        "description": "Zero amount: 0",
        "run": lambda: solution([1], 0),
        "expected": 0,
    },
    {
        "description": "Single coin: coins=[1] amount=5 -> 5",
        "run": lambda: solution([1], 5),
        "expected": 5,
    },
    {
        "description": "Multiple options: coins=[1,2,5] amount=11 -> 3",
        "run": lambda: solution([1, 2, 5], 11),
        "expected": 3,
    },
]
