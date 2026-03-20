from problems.p317_reverse_words_in_a_string import solution

TEST_CASES = [
    {
        "description": "Basic: the sky is blue",
        "run": lambda: solution("the sky is blue"),
        "expected": "blue is sky the",
    },
    {
        "description": "Leading/trailing spaces",
        "run": lambda: solution("  hello world  "),
        "expected": "world hello",
    },
    {
        "description": "Multiple spaces between words",
        "run": lambda: solution("a good   example"),
        "expected": "example good a",
    },
    {
        "description": "Single word",
        "run": lambda: solution("hello"),
        "expected": "hello",
    },
]
