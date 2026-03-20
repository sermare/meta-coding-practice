from problems.p777_count_asterisks import solution

TEST_CASES = [
    {
        "description": "Basic: 'l|*e*et|c**o|*de|'",
        "run": lambda: solution("l|*e*et|c**o|*de|"),
        "expected": 2,
    },
    {
        "description": "No bars: 'a*b*c'",
        "run": lambda: solution("a*b*c"),
        "expected": 2,
    },
    {
        "description": "All inside bars: '|*|*|*|'",
        "run": lambda: solution("|*|*|*|"),
        "expected": 1,
    },
    {
        "description": "No asterisks: 'abc|def|ghi'",
        "run": lambda: solution("abc|def|ghi"),
        "expected": 0,
    },
]
