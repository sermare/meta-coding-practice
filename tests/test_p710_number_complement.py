from problems.p710_number_complement import solution

TEST_CASES = [
    {
        "description": "Basic case: num=5",
        "run": lambda: solution(5),
        "expected": 2,
    },
    {
        "description": "Single bit: num=1",
        "run": lambda: solution(1),
        "expected": 0,
    },
    {
        "description": "All ones in binary: num=7",
        "run": lambda: solution(7),
        "expected": 0,
    },
    {
        "description": "Power of two: num=8",
        "run": lambda: solution(8),
        "expected": 7,
    },
    {
        "description": "Larger number: num=10",
        "run": lambda: solution(10),
        "expected": 5,
    },
]
