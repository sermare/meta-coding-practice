from problems.p308_best_time_to_buy_and_sell_stock_ii import solution

TEST_CASES = [
    {
        "description": "Basic case: [7,1,5,3,6,4]",
        "run": lambda: solution([7, 1, 5, 3, 6, 4]),
        "expected": 7,
    },
    {
        "description": "Always increasing: [1,2,3,4,5]",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": 4,
    },
    {
        "description": "Always decreasing: [7,6,4,3,1]",
        "run": lambda: solution([7, 6, 4, 3, 1]),
        "expected": 0,
    },
    {
        "description": "Single element",
        "run": lambda: solution([5]),
        "expected": 0,
    },
]
