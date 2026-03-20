from problems.p242_count_and_say import solution

TEST_CASES = [
    {
        "description": "n=1",
        "run": lambda: solution(1),
        "expected": "1",
    },
    {
        "description": "n=2",
        "run": lambda: solution(2),
        "expected": "11",
    },
    {
        "description": "n=3",
        "run": lambda: solution(3),
        "expected": "21",
    },
    {
        "description": "n=4",
        "run": lambda: solution(4),
        "expected": "1211",
    },
    {
        "description": "n=5",
        "run": lambda: solution(5),
        "expected": "111221",
    },
]
