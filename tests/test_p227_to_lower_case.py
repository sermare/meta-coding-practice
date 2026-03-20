from problems.p227_to_lower_case import solution

TEST_CASES = [
    {
        "description": "Mixed case: Hello",
        "run": lambda: solution("Hello"),
        "expected": "hello",
    },
    {
        "description": "All uppercase: LOVELY",
        "run": lambda: solution("LOVELY"),
        "expected": "lovely",
    },
    {
        "description": "Already lowercase: here",
        "run": lambda: solution("here"),
        "expected": "here",
    },
    {
        "description": "With numbers: Hello123",
        "run": lambda: solution("Hello123"),
        "expected": "hello123",
    },
    {
        "description": "Empty string",
        "run": lambda: solution(""),
        "expected": "",
    },
]
