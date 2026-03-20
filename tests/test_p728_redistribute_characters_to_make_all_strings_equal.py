from problems.p728_redistribute_characters_to_make_all_strings_equal import solution

TEST_CASES = [
    {
        "description": "Can make equal: ['abc','aabc','bc']",
        "run": lambda: solution(["abc", "aabc", "bc"]),
        "expected": True,
    },
    {
        "description": "Cannot make equal: ['ab','a']",
        "run": lambda: solution(["ab", "a"]),
        "expected": False,
    },
    {
        "description": "Single string: ['abc']",
        "run": lambda: solution(["abc"]),
        "expected": True,
    },
    {
        "description": "All empty: ['','','']",
        "run": lambda: solution(["", "", ""]),
        "expected": True,
    },
]
