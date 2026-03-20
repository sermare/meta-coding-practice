from problems.p758_sum_of_digits_of_string_after_convert import solution

TEST_CASES = [
    {
        "description": "iiii with k=1",
        "run": lambda: solution("iiii", 1),
        "expected": 36,
    },
    {
        "description": "leetcode with k=2",
        "run": lambda: solution("leetcode", 2),
        "expected": 6,
    },
    {
        "description": "zbax with k=2",
        "run": lambda: solution("zbax", 2),
        "expected": 8,
    },
    {
        "description": "a with k=1",
        "run": lambda: solution("a", 1),
        "expected": 1,
    },
]
