from problems.p171_longest_substring_with_at_most_k_distinct_characters import solution

TEST_CASES = [
    {
        "description": "eceba, k=2 -> 3",
        "run": lambda: solution("eceba", 2),
        "expected": 3,
    },
    {
        "description": "aa, k=1 -> 2",
        "run": lambda: solution("aa", 1),
        "expected": 2,
    },
    {
        "description": "Empty string -> 0",
        "run": lambda: solution("", 2),
        "expected": 0,
    },
    {
        "description": "k=0 -> 0",
        "run": lambda: solution("abc", 0),
        "expected": 0,
    },
    {
        "description": "All distinct, k >= len",
        "run": lambda: solution("abc", 3),
        "expected": 3,
    },
]
