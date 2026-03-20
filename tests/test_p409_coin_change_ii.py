from problems.p409_coin_change_ii import solution

TEST_CASES = [
    {
        "description": "Basic: amount=5, coins=[1,2,5]",
        "run": lambda: solution(5, [1, 2, 5]),
        "expected": 4,
    },
    {
        "description": "No way: amount=3, coins=[2]",
        "run": lambda: solution(3, [2]),
        "expected": 0,
    },
    {
        "description": "Zero amount: amount=0, coins=[1,2]",
        "run": lambda: solution(0, [1, 2]),
        "expected": 1,
    },
    {
        "description": "Single coin: amount=5, coins=[5]",
        "run": lambda: solution(5, [5]),
        "expected": 1,
    },
    {
        "description": "Multiple coins: amount=10, coins=[1,2,5]",
        "run": lambda: solution(10, [1, 2, 5]),
        "expected": 10,
    },
]
