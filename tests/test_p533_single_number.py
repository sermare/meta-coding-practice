from problems.p533_single_number import solution

TEST_CASES = [
    {
        "description": "Basic case",
        "run": lambda: solution([2,2,1]),
        "expected": 1,
    },
    {
        "description": "Longer array",
        "run": lambda: solution([4,1,2,1,2]),
        "expected": 4,
    },
    {
        "description": "Single element",
        "run": lambda: solution([1]),
        "expected": 1,
    },
    {
        "description": "Negative numbers",
        "run": lambda: solution([-1,-1,5]),
        "expected": 5,
    },
    {
        "description": "Zero is single",
        "run": lambda: solution([0,3,3]),
        "expected": 0,
    },
]
