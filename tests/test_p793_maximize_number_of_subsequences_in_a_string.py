from problems.p793_maximize_number_of_subsequences_in_a_string import solution

TEST_CASES = [
    {
        "description": "Basic: text='abdcdbc', pattern='ac'",
        "run": lambda: solution("abdcdbc", "ac"),
        "expected": 4,
    },
    {
        "description": "Same chars: text='aabb', pattern='ab'",
        "run": lambda: solution("aabb", "ab"),
        "expected": 6,
    },
    {
        "description": "No pattern chars: text='xyz', pattern='ab'",
        "run": lambda: solution("xyz", "ab"),
        "expected": 0,
    },
    {
        "description": "Same pattern chars: text='aa', pattern='aa'",
        "run": lambda: solution("aa", "aa"),
        "expected": 3,
    },
]
