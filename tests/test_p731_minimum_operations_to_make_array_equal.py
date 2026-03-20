from problems.p731_minimum_operations_to_make_array_equal import solution

TEST_CASES = [
    {
        "description": "n=3: arr=[1,3,5]",
        "run": lambda: solution(3),
        "expected": 2,
    },
    {
        "description": "n=6: arr=[1,3,5,7,9,11]",
        "run": lambda: solution(6),
        "expected": 9,
    },
    {
        "description": "n=1: single element",
        "run": lambda: solution(1),
        "expected": 0,
    },
    {
        "description": "n=4: arr=[1,3,5,7]",
        "run": lambda: solution(4),
        "expected": 4,
    },
]
