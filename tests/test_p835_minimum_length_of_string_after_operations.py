from problems.p835_minimum_length_of_string_after_operations import solution

TEST_CASES = [
    {
        "description": "Basic: abaacbcbb",
        "run": lambda: solution("abaacbcbb"),
        "expected": 5,
    },
    {
        "description": "All same: aaa",
        "run": lambda: solution("aaa"),
        "expected": 1,
    },
    {
        "description": "No duplicates: abc",
        "run": lambda: solution("abc"),
        "expected": 3,
    },
    {
        "description": "Single char: a",
        "run": lambda: solution("a"),
        "expected": 1,
    },
]
