from problems.p446_maximum_length_of_concatenated_string_with_unique_characters import solution

TEST_CASES = [
    {
        "description": "Basic: ['un','iq','ue']",
        "run": lambda: solution(["un", "iq", "ue"]),
        "expected": 4,
    },
    {
        "description": "With conflicts: ['cha','r','act','ers']",
        "run": lambda: solution(["cha", "r", "act", "ers"]),
        "expected": 6,
    },
    {
        "description": "All conflict: ['abcdefghijklmnopqrstuvwxyz']",
        "run": lambda: solution(["abcdefghijklmnopqrstuvwxyz"]),
        "expected": 26,
    },
    {
        "description": "Self duplicate: ['aa','bb']",
        "run": lambda: solution(["aa", "bb"]),
        "expected": 0,
    },
    {
        "description": "Empty array",
        "run": lambda: solution([]),
        "expected": 0,
    },
]
