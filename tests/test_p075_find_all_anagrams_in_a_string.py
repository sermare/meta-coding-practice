from problems.p075_find_all_anagrams_in_a_string import solution

TEST_CASES = [
    {
        "description": "Standard: s=cbaebabacd, p=abc",
        "run": lambda: solution("cbaebabacd", "abc"),
        "expected": [0, 6],
    },
    {
        "description": "Overlapping: s=abab, p=ab",
        "run": lambda: solution("abab", "ab"),
        "expected": [0, 1, 2],
    },
    {
        "description": "No match: s=hello, p=xyz",
        "run": lambda: solution("hello", "xyz"),
        "expected": [],
    },
    {
        "description": "Single char match: s=a, p=a",
        "run": lambda: solution("a", "a"),
        "expected": [0],
    },
]
