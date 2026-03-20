from problems.p746_check_if_all_characters_have_equal_number_of_occurrences import solution

TEST_CASES = [
    {
        "description": "Equal occurrences: 'abacbc'",
        "run": lambda: solution("abacbc"),
        "expected": True,
    },
    {
        "description": "Unequal: 'aaabb'",
        "run": lambda: solution("aaabb"),
        "expected": False,
    },
    {
        "description": "Single char: 'a'",
        "run": lambda: solution("a"),
        "expected": True,
    },
    {
        "description": "All same: 'aaaa'",
        "run": lambda: solution("aaaa"),
        "expected": True,
    },
    {
        "description": "Two chars equal: 'aabb'",
        "run": lambda: solution("aabb"),
        "expected": True,
    },
]
