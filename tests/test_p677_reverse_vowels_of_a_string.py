from problems.p677_reverse_vowels_of_a_string import solution

TEST_CASES = [
    {
        "description": "Basic: hello -> holle",
        "run": lambda: solution("hello"),
        "expected": "holle",
    },
    {
        "description": "Mixed case: leetcode -> leotcede",
        "run": lambda: solution("leetcode"),
        "expected": "leotcede",
    },
    {
        "description": "No vowels: xyz",
        "run": lambda: solution("xyz"),
        "expected": "xyz",
    },
    {
        "description": "All vowels: aeiou",
        "run": lambda: solution("aeiou"),
        "expected": "uoiea",
    },
    {
        "description": "Single character",
        "run": lambda: solution("a"),
        "expected": "a",
    },
]
