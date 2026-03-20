from problems.p100_happy_number import solution

TEST_CASES = [
    {
        "description": "Happy number: 19",
        "run": lambda: solution(19),
        "expected": True,
    },
    {
        "description": "Not happy: 2",
        "run": lambda: solution(2),
        "expected": False,
    },
    {
        "description": "Happy number: 1",
        "run": lambda: solution(1),
        "expected": True,
    },
    {
        "description": "Happy number: 7",
        "run": lambda: solution(7),
        "expected": True,
    },
    {
        "description": "Not happy: 4",
        "run": lambda: solution(4),
        "expected": False,
    },
]
