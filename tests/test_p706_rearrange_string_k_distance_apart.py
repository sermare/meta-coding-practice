from problems.p706_rearrange_string_k_distance_apart import solution

TEST_CASES = [
    {
        "description": "Basic case: s='aabbcc', k=3",
        "run": lambda: solution("aabbcc", 3),
        "expected": "abcabc",
    },
    {
        "description": "Impossible case: s='aaabc', k=3",
        "run": lambda: solution("aaabc", 3),
        "expected": "",
    },
    {
        "description": "k=0 returns original: s='aabbcc', k=0",
        "run": lambda: solution("aabbcc", 0),
        "expected": "aabbcc",
    },
    {
        "description": "Single char: s='a', k=1",
        "run": lambda: solution("a", 1),
        "expected": "a",
    },
    {
        "description": "All same chars: s='aaaa', k=2",
        "run": lambda: solution("aaaa", 2),
        "expected": "",
    },
]
