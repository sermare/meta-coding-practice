from problems.p748_capitalize_the_title import solution

TEST_CASES = [
    {
        "description": "Basic case: 'capiTalIze tHe titLe'",
        "run": lambda: solution("capiTalIze tHe titLe"),
        "expected": "Capitalize the Title",
    },
    {
        "description": "Short words only: 'i lOve to cOdE'",
        "run": lambda: solution("i lOve to cOdE"),
        "expected": "i Love to Code",
    },
    {
        "description": "All short: 'me is an'",
        "run": lambda: solution("me is an"),
        "expected": "me is an",
    },
    {
        "description": "Single long word: 'HELLO'",
        "run": lambda: solution("HELLO"),
        "expected": "Hello",
    },
]
