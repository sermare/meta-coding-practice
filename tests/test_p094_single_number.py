from problems.p094_single_number import solution

TEST_CASES = [
    {
        "description": "Basic: [2,2,1] -> 1",
        "run": lambda: solution([2, 2, 1]),
        "expected": 1,
    },
    {
        "description": "Longer: [4,1,2,1,2] -> 4",
        "run": lambda: solution([4, 1, 2, 1, 2]),
        "expected": 4,
    },
    {
        "description": "Single element: [1]",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "Negative numbers: [-1,2,-1]",
        "run": lambda: solution([-1, 2, -1]),
        "expected": 2,
    },
]
