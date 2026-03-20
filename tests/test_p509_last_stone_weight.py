from problems.p509_last_stone_weight import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution([2,7,4,1,8,1]),
        "expected": 1,
    },
    {
        "description": "Single stone",
        "run": lambda: solution([5]),
        "expected": 5,
    },
    {
        "description": "Two equal stones",
        "run": lambda: solution([3,3]),
        "expected": 0,
    },
    {
        "description": "Two unequal stones",
        "run": lambda: solution([5,3]),
        "expected": 2,
    },
    {
        "description": "All same weight",
        "run": lambda: solution([2,2,2,2]),
        "expected": 0,
    },
]
