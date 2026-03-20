from problems.p318_substring_with_concatenation_of_all_words import solution

TEST_CASES = [
    {
        "description": "Basic: barfoothefoobarman with [foo,bar]",
        "run": lambda: sorted(solution("barfoothefoobarman", ["foo", "bar"])),
        "expected": [0, 9],
    },
    {
        "description": "No match: wordgoodgoodgoodbestword",
        "run": lambda: solution("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
        "expected": [],
    },
    {
        "description": "Overlapping: barfoofoobarthefoobarman",
        "run": lambda: sorted(solution("barfoofoobarthefoobarman", ["bar", "foo", "the"])),
        "expected": [6, 9, 12],
    },
    {
        "description": "Single word",
        "run": lambda: solution("foobar", ["foo"]),
        "expected": [0],
    },
]
