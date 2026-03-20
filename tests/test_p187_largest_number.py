from problems.p187_largest_number import solution

TEST_CASES = [
    {
        "description": "[10,2] -> 210",
        "run": lambda: solution([10, 2]),
        "expected": "210",
    },
    {
        "description": "[3,30,34,5,9] -> 9534330",
        "run": lambda: solution([3, 30, 34, 5, 9]),
        "expected": "9534330",
    },
    {
        "description": "All zeros",
        "run": lambda: solution([0, 0]),
        "expected": "0",
    },
    {
        "description": "Single number",
        "run": lambda: solution([1]),
        "expected": "1",
    },
]
