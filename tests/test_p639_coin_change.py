from problems.p639_coin_change import solution

TEST_CASES = [
    {
        "description": "Basic case: coins=[1,5,10] amount=12",
        "run": lambda: solution([1, 5, 10], 12),
        "expected": 3,
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
        "description": "Standard coins: coins=[1,2,5] amount=11",
        "run": lambda: solution([1, 2, 5], 11),
        "expected": 3,
    },
]
