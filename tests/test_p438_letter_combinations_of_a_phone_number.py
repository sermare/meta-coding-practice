from problems.p438_letter_combinations_of_a_phone_number import solution

TEST_CASES = [
    {
        "description": "Two digits: 23",
        "run": lambda: sorted(solution("23")),
        "expected": sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    },
    {
        "description": "Empty string",
        "run": lambda: solution(""),
        "expected": [],
    },
    {
        "description": "Single digit: 2",
        "run": lambda: sorted(solution("2")),
        "expected": ["a", "b", "c"],
    },
    {
        "description": "Digit with 4 letters: 7",
        "run": lambda: sorted(solution("7")),
        "expected": ["p", "q", "r", "s"],
    },
    {
        "description": "Count for three digits: 234",
        "run": lambda: len(solution("234")),
        "expected": 27,
    },
]
