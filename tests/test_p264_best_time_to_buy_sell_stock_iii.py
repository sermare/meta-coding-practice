from problems.p264_best_time_to_buy_sell_stock_iii import solution

TEST_CASES = [
    {
        "description": "[3,3,5,0,0,3,1,4] -> 6",
        "run": lambda: solution([3, 3, 5, 0, 0, 3, 1, 4]),
        "expected": 6,
    },
    {
        "description": "[1,2,3,4,5] -> 4",
        "run": lambda: solution([1, 2, 3, 4, 5]),
        "expected": 4,
    },
    {
        "description": "[7,6,4,3,1] -> 0 (decreasing)",
        "run": lambda: solution([7, 6, 4, 3, 1]),
        "expected": 0,
    },
    {
        "description": "[1] -> 0 (single day)",
        "run": lambda: solution([1]),
        "expected": 0,
    },
    {
        "description": "[1,2,4,2,5,7,2,4,9,0] -> 13",
        "run": lambda: solution([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]),
        "expected": 13,
    },
]
