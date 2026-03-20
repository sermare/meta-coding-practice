from problems.p131_longest_string_chain import solution

TEST_CASES = [
    {
        "description": "Standard chain",
        "run": lambda: solution(["a", "b", "ba", "bca", "bda", "bdca"]),
        "expected": 4,
    },
    {
        "description": "All same length, no chain",
        "run": lambda: solution(["ab", "cd", "ef"]),
        "expected": 1,
    },
    {
        "description": "Single word",
        "run": lambda: solution(["xyz"]),
        "expected": 1,
    },
    {
        "description": "Another chain example",
        "run": lambda: solution(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]),
        "expected": 5,
    },
    {
        "description": "Two separate chains",
        "run": lambda: solution(["a", "ab", "abc", "x", "xy"]),
        "expected": 3,
    },
]
