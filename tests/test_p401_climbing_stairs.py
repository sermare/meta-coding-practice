from problems.p401_climbing_stairs import solution

TEST_CASES = [
    {
        "description": "Base case: n=1",
        "run": lambda: solution(1),
        "expected": 1,
    },
    {
        "description": "Two steps: n=2",
        "run": lambda: solution(2),
        "expected": 2,
    },
    {
        "description": "Three steps: n=3",
        "run": lambda: solution(3),
        "expected": 3,
    },
    {
        "description": "Five steps: n=5",
        "run": lambda: solution(5),
        "expected": 8,
    },
    {
        "description": "Ten steps: n=10",
        "run": lambda: solution(10),
        "expected": 89,
    },
]
