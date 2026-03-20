from problems.p204_reverse_bits import solution

TEST_CASES = [
    {
        "description": "Example 1: 43261596",
        "run": lambda: solution(43261596),
        "expected": 964176192,
    },
    {
        "description": "Example 2: 4294967293",
        "run": lambda: solution(4294967293),
        "expected": 3221225471,
    },
    {
        "description": "All zeros: 0",
        "run": lambda: solution(0),
        "expected": 0,
    },
    {
        "description": "One: 1",
        "run": lambda: solution(1),
        "expected": 2147483648,
    },
    {
        "description": "All ones: 4294967295",
        "run": lambda: solution(4294967295),
        "expected": 4294967295,
    },
]
