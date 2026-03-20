from problems.p797_percentage_of_letter_in_string import solution

TEST_CASES = [
    {
        "description": "Basic: 'foobar', letter='o'",
        "run": lambda: solution("foobar", "o"),
        "expected": 33,
    },
    {
        "description": "All same: 'aaaa', letter='a'",
        "run": lambda: solution("aaaa", "a"),
        "expected": 100,
    },
    {
        "description": "None present: 'abc', letter='z'",
        "run": lambda: solution("abc", "z"),
        "expected": 0,
    },
    {
        "description": "Half: 'aabb', letter='a'",
        "run": lambda: solution("aabb", "a"),
        "expected": 50,
    },
]
