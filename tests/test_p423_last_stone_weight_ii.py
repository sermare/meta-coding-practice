from problems.p423_last_stone_weight_ii import solution

TEST_CASES = [
    {
        "description": "Basic: [2,7,4,1,8,1]",
        "run": lambda: solution([2, 7, 4, 1, 8, 1]),
        "expected": 1,
    },
    {
        "description": "Equal stones: [31,26,33,21,40]",
        "run": lambda: solution([31, 26, 33, 21, 40]),
        "expected": 5,
    },
    {
        "description": "Single stone: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "Two equal: [5,5]",
        "run": lambda: solution([5, 5]),
        "expected": 0,
    },
    {
        "description": "Small stones: [1,2]",
        "run": lambda: solution([1, 2]),
        "expected": 1,
    },
]
