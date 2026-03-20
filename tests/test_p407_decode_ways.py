from problems.p407_decode_ways import solution

TEST_CASES = [
    {
        "description": "Three ways: 226",
        "run": lambda: solution("226"),
        "expected": 3,
    },
    {
        "description": "Single digit: 6",
        "run": lambda: solution("6"),
        "expected": 1,
    },
    {
        "description": "Leading zero: 06",
        "run": lambda: solution("06"),
        "expected": 0,
    },
    {
        "description": "Two digits: 12",
        "run": lambda: solution("12"),
        "expected": 2,
    },
    {
        "description": "Longer string: 11106",
        "run": lambda: solution("11106"),
        "expected": 2,
    },
]
