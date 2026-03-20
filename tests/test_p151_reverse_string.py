from problems.p151_reverse_string import solution

TEST_CASES = [
    {
        "description": "Basic: hello -> olleh",
        "run": lambda: solution(["h", "e", "l", "l", "o"]),
        "expected": ["o", "l", "l", "e", "h"],
    },
    {
        "description": "Palindrome name: Hannah",
        "run": lambda: solution(["H", "a", "n", "n", "a", "h"]),
        "expected": ["h", "a", "n", "n", "a", "H"],
    },
    {
        "description": "Single character",
        "run": lambda: solution(["a"]),
        "expected": ["a"],
    },
    {
        "description": "Two characters",
        "run": lambda: solution(["a", "b"]),
        "expected": ["b", "a"],
    },
    {
        "description": "Already palindrome",
        "run": lambda: solution(["a", "b", "a"]),
        "expected": ["a", "b", "a"],
    },
]
