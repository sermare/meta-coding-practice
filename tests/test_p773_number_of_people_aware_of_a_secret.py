from problems.p773_number_of_people_aware_of_a_secret import solution

TEST_CASES = [
    {
        "description": "n=6, delay=2, forget=4",
        "run": lambda: solution(6, 2, 4),
        "expected": 5,
    },
    {
        "description": "n=4, delay=1, forget=3",
        "run": lambda: solution(4, 1, 3),
        "expected": 6,
    },
    {
        "description": "n=1, delay=1, forget=2",
        "run": lambda: solution(1, 1, 2),
        "expected": 1,
    },
    {
        "description": "n=2, delay=1, forget=2",
        "run": lambda: solution(2, 1, 2),
        "expected": 1,
    },
]
