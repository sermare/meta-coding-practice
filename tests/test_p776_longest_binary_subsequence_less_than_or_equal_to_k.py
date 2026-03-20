from problems.p776_longest_binary_subsequence_less_than_or_equal_to_k import solution

TEST_CASES = [
    {
        "description": "Basic: s='1001010', k=5",
        "run": lambda: solution("1001010", 5),
        "expected": 5,
    },
    {
        "description": "All zeros: s='00101001', k=1",
        "run": lambda: solution("00101001", 1),
        "expected": 6,
    },
    {
        "description": "Single char: s='1', k=1",
        "run": lambda: solution("1", 1),
        "expected": 1,
    },
    {
        "description": "All ones: s='111', k=3",
        "run": lambda: solution("111", 3),
        "expected": 2,
    },
]
