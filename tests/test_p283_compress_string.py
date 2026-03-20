from problems.p283_compress_string import solution

TEST_CASES = [
    {
        "description": "['a','a','b','b','c','c','c'] -> 6",
        "run": lambda: solution(["a","a","b","b","c","c","c"]),
        "expected": 6,
    },
    {
        "description": "['a'] -> 1",
        "run": lambda: solution(["a"]),
        "expected": 1,
    },
    {
        "description": "['a','b','b','b','b','b','b','b','b','b','b','b','b'] -> 4",
        "run": lambda: solution(["a","b","b","b","b","b","b","b","b","b","b","b","b"]),
        "expected": 4,
    },
    {
        "description": "['a','b','c'] -> 3 (no compression)",
        "run": lambda: solution(["a","b","c"]),
        "expected": 3,
    },
    {
        "description": "['a','a','a','a','a','a','a','a','a','a'] -> 3",
        "run": lambda: solution(["a","a","a","a","a","a","a","a","a","a"]),
        "expected": 3,
    },
]
