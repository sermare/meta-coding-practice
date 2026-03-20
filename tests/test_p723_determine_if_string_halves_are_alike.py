from problems.p723_determine_if_string_halves_are_alike import solution

TEST_CASES = [
    {
        "description": "Alike: 'book'",
        "run": lambda: solution("book"),
        "expected": True,
    },
    {
        "description": "Not alike: 'textbook'",
        "run": lambda: solution("textbook"),
        "expected": False,
    },
    {
        "description": "Alike with uppercase: 'MerryChristmas'",
        "run": lambda: solution("MerryChristmas"),
        "expected": False,
    },
    {
        "description": "Alike: 'AbCdEfGh'",
        "run": lambda: solution("AbCdEfGh"),
        "expected": True,
    },
]
