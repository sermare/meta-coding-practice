from problems.p669_collapsing_string import solution

TEST_CASES = [
    {
        "description": "Full collapse: aabccba -> a",
        "run": lambda: solution("aabccba"),
        "expected": "a",
    },
    {
        "description": "No collapse needed: abc",
        "run": lambda: solution("abc"),
        "expected": "abc",
    },
    {
        "description": "Complete removal: aabb",
        "run": lambda: solution("aabb"),
        "expected": "",
    },
    {
        "description": "Single character",
        "run": lambda: solution("x"),
        "expected": "x",
    },
    {
        "description": "Empty string",
        "run": lambda: solution(""),
        "expected": "",
    },
]
