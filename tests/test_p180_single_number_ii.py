from problems.p180_single_number_ii import solution

TEST_CASES = [
    {
        "description": "[2,2,3,2] -> 3",
        "run": lambda: solution([2, 2, 3, 2]),
        "expected": 3,
    },
    {
        "description": "[0,1,0,1,0,1,99] -> 99",
        "run": lambda: solution([0, 1, 0, 1, 0, 1, 99]),
        "expected": 99,
    },
    {
        "description": "Single element",
        "run": lambda: solution([5]),
        "expected": 5,
    },
    {
        "description": "Negative numbers",
        "run": lambda: solution([-2, -2, 1, -2]),
        "expected": 1,
    },
]
