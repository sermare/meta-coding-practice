from problems.p246_length_of_last_word import solution

TEST_CASES = [
    {
        "description": "Two words: Hello World",
        "run": lambda: solution("Hello World"),
        "expected": 5,
    },
    {
        "description": "Trailing spaces: fly me to the moon  ",
        "run": lambda: solution("   fly me   to   the moon  "),
        "expected": 4,
    },
    {
        "description": "Single word: luffy",
        "run": lambda: solution("luffy"),
        "expected": 5,
    },
    {
        "description": "Single char: a",
        "run": lambda: solution("a"),
        "expected": 1,
    },
    {
        "description": "Multiple spaces: a  b  c",
        "run": lambda: solution("a  b  c"),
        "expected": 1,
    },
]
