from problems.p263_distinct_subsequences import solution

TEST_CASES = [
    {
        "description": "'rabbbit','rabbit' -> 3",
        "run": lambda: solution("rabbbit", "rabbit"),
        "expected": 3,
    },
    {
        "description": "'babgbag','bag' -> 5",
        "run": lambda: solution("babgbag", "bag"),
        "expected": 5,
    },
    {
        "description": "'a','a' -> 1",
        "run": lambda: solution("a", "a"),
        "expected": 1,
    },
    {
        "description": "'a','b' -> 0",
        "run": lambda: solution("a", "b"),
        "expected": 0,
    },
    {
        "description": "'aaa','a' -> 3",
        "run": lambda: solution("aaa", "a"),
        "expected": 3,
    },
]
