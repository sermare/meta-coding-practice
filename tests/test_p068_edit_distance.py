from problems.p068_edit_distance import solution

TEST_CASES = [
    {
        "description": "horse -> ros",
        "run": lambda: solution("horse", "ros"),
        "expected": 3,
    },
    {
        "description": "intention -> execution",
        "run": lambda: solution("intention", "execution"),
        "expected": 5,
    },
    {
        "description": "Empty to abc",
        "run": lambda: solution("", "abc"),
        "expected": 3,
    },
    {
        "description": "Same strings",
        "run": lambda: solution("abc", "abc"),
        "expected": 0,
    },
    {
        "description": "Single char difference",
        "run": lambda: solution("a", "b"),
        "expected": 1,
    },
]
