from problems.p418_best_time_to_buy_sell_stock_with_cooldown import solution

TEST_CASES = [
    {
        "description": "Basic: [1,2,3,0,2]",
        "run": lambda: solution([1, 2, 3, 0, 2]),
        "expected": 3,
    },
    {
        "description": "Single price: [1]",
        "run": lambda: solution([1]),
        "expected": 0,
    },
    {
        "description": "Decreasing: [3,2,1]",
        "run": lambda: solution([3, 2, 1]),
        "expected": 0,
    },
    {
        "description": "Two prices: [1,2]",
        "run": lambda: solution([1, 2]),
        "expected": 1,
    },
    {
        "description": "Increasing: [1,2,3,4,5]",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": 4,
    },
]
