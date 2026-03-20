from problems.p756_check_if_string_is_a_prefix_of_array import solution

TEST_CASES = [
    {
        "description": "Valid prefix: iloveleetcode",
        "run": lambda: solution("iloveleetcode", ["i","love","leetcode","apples"]),
        "expected": True,
    },
    {
        "description": "Not a prefix: iloveleetcode with wrong words",
        "run": lambda: solution("iloveleetcode", ["apples","i","love","leetcode"]),
        "expected": False,
    },
    {
        "description": "Single word match",
        "run": lambda: solution("abc", ["abc","def"]),
        "expected": True,
    },
    {
        "description": "Partial word not valid",
        "run": lambda: solution("ab", ["abc","def"]),
        "expected": False,
    },
]
