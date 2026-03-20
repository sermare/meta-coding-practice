from problems.p549_count_primes import solution

TEST_CASES = [
    {
        "description": "Primes below 10",
        "run": lambda: solution(10),
        "expected": 4,
    },
    {
        "description": "n=0",
        "run": lambda: solution(0),
        "expected": 0,
    },
    {
        "description": "n=1",
        "run": lambda: solution(1),
        "expected": 0,
    },
    {
        "description": "n=2",
        "run": lambda: solution(2),
        "expected": 0,
    },
    {
        "description": "n=20",
        "run": lambda: solution(20),
        "expected": 8,
    },
]
