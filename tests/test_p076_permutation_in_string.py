from problems.p076_permutation_in_string import solution

TEST_CASES = [
    {
        "description": "Found: s1=ab, s2=eidbaooo",
        "run": lambda: solution("ab", "eidbaooo"),
        "expected": True,
    },
    {
        "description": "Not found: s1=ab, s2=eidboaoo",
        "run": lambda: solution("ab", "eidboaoo"),
        "expected": False,
    },
    {
        "description": "Exact match: s1=abc, s2=bca",
        "run": lambda: solution("abc", "bca"),
        "expected": True,
    },
    {
        "description": "Longer s1 than s2: s1=abc, s2=ab",
        "run": lambda: solution("abc", "ab"),
        "expected": False,
    },
]
