from problems.p541_happy_number import solution

TEST_CASES = [
    {
        "description": "Happy number",
        "run": lambda: solution(19),
        "expected": True,
    },
    {
        "description": "Not happy",
        "run": lambda: solution(2),
        "expected": False,
    },
    {
        "description": "One is happy",
        "run": lambda: solution(1),
        "expected": True,
    },
    {
        "description": "Seven is happy",
        "run": lambda: solution(7),
        "expected": True,
    },
    {
        "description": "Four is not happy",
        "run": lambda: solution(4),
        "expected": False,
    },
]
