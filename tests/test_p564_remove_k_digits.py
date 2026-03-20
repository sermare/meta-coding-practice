from problems.p564_remove_k_digits import solution

TEST_CASES = [
    {
        "description": "Remove 3: 1432219 -> 1219",
        "run": lambda: solution("1432219", 3),
        "expected": "1219",
    },
    {
        "description": "Leading zero: 10200, k=1 -> 200",
        "run": lambda: solution("10200", 1),
        "expected": "200",
    },
    {
        "description": "Remove all: 10, k=2 -> 0",
        "run": lambda: solution("10", 2),
        "expected": "0",
    },
    {
        "description": "Remove 1: 9, k=1 -> 0",
        "run": lambda: solution("9", 1),
        "expected": "0",
    },
    {
        "description": "Remove none: 123, k=0 -> 123",
        "run": lambda: solution("123", 0),
        "expected": "123",
    },
]
