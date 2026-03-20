from problems.p172_string_compression import solution

TEST_CASES = [
    {
        "description": "Mixed repeats",
        "run": lambda: solution(["a","a","b","b","c","c","c"]),
        "expected": 6,
    },
    {
        "description": "Single char",
        "run": lambda: solution(["a"]),
        "expected": 1,
    },
    {
        "description": "12 b's -> b12 (4 chars)",
        "run": lambda: solution(["a","b","b","b","b","b","b","b","b","b","b","b","b"]),
        "expected": 4,
    },
    {
        "description": "No repeats",
        "run": lambda: solution(["a","b","c"]),
        "expected": 3,
    },
]
