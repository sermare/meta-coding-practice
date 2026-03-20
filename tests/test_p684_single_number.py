from problems.p684_single_number import solution

TEST_CASES = [
    {
        "description": "Basic: [2,2,1]",
        "run": lambda: solution([2, 2, 1]),
        "expected": 1,
    },
    {
        "description": "Larger: [4,1,2,1,2]",
        "run": lambda: solution([4, 1, 2, 1, 2]),
        "expected": 4,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "Negative numbers: [-1,-1,2]",
        "run": lambda: solution([-1, -1, 2]),
        "expected": 2,
    },
]
