from problems.p157_count_primes import solution

TEST_CASES = [
    {
        "description": "n=10 -> 4 primes",
        "run": lambda: solution(10),
        "expected": 4,
    },
    {
        "description": "n=0 -> 0",
        "run": lambda: solution(0),
        "expected": 0,
    },
    {
        "description": "n=1 -> 0",
        "run": lambda: solution(1),
        "expected": 0,
    },
    {
        "description": "n=2 -> 0 (strictly less)",
        "run": lambda: solution(2),
        "expected": 0,
    },
    {
        "description": "n=20 -> 8 primes",
        "run": lambda: solution(20),
        "expected": 8,
    },
]
