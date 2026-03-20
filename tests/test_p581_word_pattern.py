from problems.p581_word_pattern import solution

TEST_CASES = [
    {
        "description": "Matches: abba / dog cat cat dog",
        "run": lambda: solution("abba", "dog cat cat dog"),
        "expected": True,
    },
    {
        "description": "No match: abba / dog cat cat fish",
        "run": lambda: solution("abba", "dog cat cat fish"),
        "expected": False,
    },
    {
        "description": "Not bijective: aaaa / dog cat cat dog",
        "run": lambda: solution("aaaa", "dog cat cat dog"),
        "expected": False,
    },
    {
        "description": "Single char: a / dog",
        "run": lambda: solution("a", "dog"),
        "expected": True,
    },
    {
        "description": "Length mismatch: ab / dog",
        "run": lambda: solution("ab", "dog"),
        "expected": False,
    },
]
