from problems.p023_letter_combinations_of_a_phone_number import solution

TEST_CASES = [
    {
        "description": "Digits '23' produce 9 combinations",
        "run": lambda: sorted(solution("23")),
        "expected": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
    },
    {
        "description": "Empty string produces empty list",
        "run": lambda: solution(""),
        "expected": [],
    },
    {
        "description": "Single digit '2' produces ['a','b','c']",
        "run": lambda: sorted(solution("2")),
        "expected": ["a", "b", "c"],
    },
    {
        "description": "Digits '79' produce 16 combinations",
        "run": lambda: sorted(solution("79")),
        "expected": sorted([
            "pw", "px", "py", "pz",
            "qw", "qx", "qy", "qz",
            "rw", "rx", "ry", "rz",
            "sw", "sx", "sy", "sz",
        ]),
    },
]
