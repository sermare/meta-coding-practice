from problems.p284_minimum_moves_to_equal_array_elements import solution

TEST_CASES = [
    {
        "description": "[1,2,3] -> 3",
        "run": lambda: solution([1, 2, 3]),
        "expected": 3,
    },
    {
        "description": "[1,1,1] -> 0",
        "run": lambda: solution([1, 1, 1]),
        "expected": 0,
    },
    {
        "description": "[1] -> 0",
        "run": lambda: solution([1]),
        "expected": 0,
    },
    {
        "description": "[1,10] -> 9",
        "run": lambda: solution([1, 10]),
        "expected": 9,
    },
    {
        "description": "[5,6,8,8,5] -> 7",
        "run": lambda: solution([5, 6, 8, 8, 5]),
        "expected": 7,
    },
]
