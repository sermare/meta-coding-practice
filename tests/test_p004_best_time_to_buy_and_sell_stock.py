from problems.p004_best_time_to_buy_and_sell_stock import solution

TEST_CASES = [
    {
        "description": "Normal case with profit: [7,1,5,3,6,4]",
        "run": lambda: solution([7, 1, 5, 3, 6, 4]),
        "expected": 5,
    },
    {
        "description": "Decreasing prices, no profit: [7,6,4,3,1]",
        "run": lambda: solution([7, 6, 4, 3, 1]),
        "expected": 0,
    },
    {
        "description": "Two elements with profit: [1,2]",
        "run": lambda: solution([1, 2]),
        "expected": 1,
    },
    {
        "description": "Profit before dip: [2,4,1]",
        "run": lambda: solution([2, 4, 1]),
        "expected": 2,
    },
    {
        "description": "All same prices: [3,3,3]",
        "run": lambda: solution([3, 3, 3]),
        "expected": 0,
    },
]
