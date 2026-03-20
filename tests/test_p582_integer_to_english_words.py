from problems.p582_integer_to_english_words import solution

TEST_CASES = [
    {
        "description": "123 -> One Hundred Twenty Three",
        "run": lambda: solution(123),
        "expected": "One Hundred Twenty Three",
    },
    {
        "description": "12345 -> Twelve Thousand ...",
        "run": lambda: solution(12345),
        "expected": "Twelve Thousand Three Hundred Forty Five",
    },
    {
        "description": "1234567 -> One Million ...",
        "run": lambda: solution(1234567),
        "expected": "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
    },
    {
        "description": "Zero",
        "run": lambda: solution(0),
        "expected": "Zero",
    },
    {
        "description": "1000000 -> One Million",
        "run": lambda: solution(1000000),
        "expected": "One Million",
    },
]
